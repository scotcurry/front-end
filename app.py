import os
from json import JSONDecodeError

import requests
import datetime
import logging

from pytz import timezone

from flask import Flask, render_template, request
from ddtrace import tracer
from ddtrace.runtime import RuntimeMetrics
from urllib3.exceptions import HTTPError

from stub_creators.team_standings_stub import create_team_standings_stub
from helpers.uri_helper import uri_to_path_valid_path

RuntimeMetrics.enable()

app = Flask(__name__)
application = app

dev_environment = os.environ.get('DEVELOPMENT_ENVIRONMENT')

if dev_environment == 'true':
    FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - '
              '%(message)s')
else:
    FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
              '[dd.service=%(dd.service)s dd.env=%(dd.env)s '
              'dd.version=%(dd.version)s '
              'dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
              '- %(message)s')


logging.basicConfig(format=FORMAT)
logger = logging.getLogger('curryware-front-end')
logger.level = logging.DEBUG


@tracer.wrap()
@app.route('/')
@app.route('/index')
def index_page():
    logger.info('Launching app!')
    local_time = datetime.datetime.now(timezone('US/Eastern'))
    # logger.info('User agent: {}'.format(user_agent))
    current_date = '{}/{}/{}'.format(str(local_time.month), str(local_time.day),
                                     str(local_time.year), str(local_time.year))
    current_time = '{}:{}:{}'.format(str(local_time.hour), str(local_time.minute),
                                     str(local_time.second))
    app_root_path = uri_to_path_valid_path(request.base_url, dev_environment)

    logger.info('Referrer: {}'.format(request.referrer))
    logger.info('App root path: {}'.format(app_root_path))

    return render_template('index.html', title='Index Page',
                           current_time=current_time, current_date=current_date,
                           referrer=request.referrer, app_root_path=app_root_path)


@app.route('/getteams', methods=['GET'])
def get_teams():

    logger.info('Calling get_teams')
    get_teams_url = 'http://curryware-java:8080/teaminfo/getteams'
    logger.info('get_teams_url: {}'.format(get_teams_url))
    response = requests.get(get_teams_url, timeout=10)
    response_json = response.json()
    return response_json


@app.route('/getstandings', methods=['GET'])
def get_standings():

    app_path_root = uri_to_path_valid_path(request.base_url, dev_environment)
    logger.info('App root path: {}'.format(app_path_root))
    response_text = ''
    logger.info('Calling get_standings')
    if dev_environment == 'true':
        response_text = create_team_standings_stub()
    else:
        get_standings_url = 'http://curryware-yahoo-api:8087/YahooApi/GetLeagueStandings'
        logger.info('get_standings_url: {}'.format(get_standings_url))

        try:
            response = requests.get(get_standings_url, timeout=10)
            response_text = response.json()
            logger.info('getstandings - Response Text: {0}'.format(response_text))
        except HTTPError as httpError:
            logger.error(httpError)
            return httpError

    return render_template('standings.html', all_teams=response_text,
                           title='Standings', app_root_path=app_path_root)


@app.route('/gettransactions', methods=['GET'])
def get_transactions():
    return 'Work in Progress'


@app.route('/getoauthtoken', methods=['GET'])
def get_oauth_token():

    headers = request.headers
    # for key, value in headers.items():
    #    logger.debug(f'Key: {key}, Value: {value}')
    logger.info('Calling get_oauth_token')
    get_oauth_token_url = 'http://curryware-yahoo-api:8087/YahooApi/GetOAuthToken'
    logger.info('get_oauth_token_url: {}'.format(get_oauth_token_url))
    try:
        response = requests.get(get_oauth_token_url, timeout=10)
        if response.status_code != 200:
            logger.error('Error getting oauth token!')
            return 'Error getting oauth token!'
        return response.text
    except HTTPError as httpError:
        logger.error(httpError)
        return None
    except JSONDecodeError as decodeError:
        logger.error('JSON Decode Error: {}'.format(decodeError.msg))
        return None


@app.route('/throw_error', methods=['GET'])
def throw_error():
    logger.info('Calling throw_error')
    scot = 1 / 0
    return scot


@app.route('/throw_java_error', methods=['GET'])
def throw_java_error():
    logger.info('Calling throw_java_error')
    java_error_url = "http://curryware-java:8080/jokes/throw_java_error"
    response = requests.get(java_error_url, timeout=10)
    response_json = response.json()
    return response_json


@app.route('/get_firebase_auth_key', methods=['GET'])
def get_firebase_auth_key():
    logger.info('Calling get_firebase_auth_key')
    try:
        auth_key_url = 'http://curryware-firebase-auth-service/get_oauth_token'
        response = requests.get(auth_key_url, timeout=10)
        response_json = response.json()
        return response_json
    except ValueError as exception:
        return 'Error getting firebase auth key!'


@app.route('/webhook_dora_incident', methods=['POST'])
def create_dora_incident_event():
    logger.info('Calling create_dora_incident_event')

    # Retrieve the relevant fields
    datadog_service = ''
    datadog_team = ''
    incident_description = ''
    incident_severity = ''

    try:
        incident_content = request.get_json()
        datadog_service = incident_content['data']['attributes']['services'][0]
        datadog_team = incident_content['data']['attributes']['team']
        incident_description = incident_content['data']['attributes']['incident_description']
        incident_severity = incident_content['data']['attributes']['severity']
        logger.info('Datadog Service: {}, Datadog Team: {}, Description: {}, Severity: {}'
                    .format(datadog_service, datadog_team, incident_description,
                            incident_severity))
    except JSONDecodeError as error:
        logger.error('JSON Decode Error: {}'.format(error))
        return 'JSON Decode Error!'

    if datadog_service != '' and datadog_team != '':
        dora_json = {'dora': 'input'}
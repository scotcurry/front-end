import os
import requests
import datetime
import logging

from pytz import timezone

from flask import Flask, render_template, request
from ddtrace import tracer
from ddtrace.runtime import RuntimeMetrics

RuntimeMetrics.enable()

app = Flask(__name__)
application = app

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
def index_page():
    logger.info('Launching app!')
    local_time = datetime.datetime.now(timezone('US/Eastern'))
    user_agent = request.headers.get('User-Agent')
    # logger.info('User agent: {}'.format(user_agent))
    current_date = '{}/{}/{}'.format(str(local_time.month), str(local_time.day),
                                     str(local_time.year), str(local_time.year))
    current_time = '{}:{}:{}'.format(str(local_time.hour), str(local_time.minute),
                                     str(local_time.second))

    log_environment_variable = os.environ.get('DD_LOGS_INJECTION')

    return render_template('index.html', title='Index Page', current_time=current_time,
                           current_date=current_date, user_agent=user_agent,
                           logs_injection_variable=log_environment_variable)


@app.route('/getteams', methods=['GET'])
def get_teams():

    logger.info('Calling get_teams')
    get_teams_url = 'http://curryware-java:8080/teaminfo/getteams'
    response = requests.get(get_teams_url, timeout=10)
    response_json = response.json()
    return response_json


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

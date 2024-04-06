import os
import datetime
import logging

from flask import Flask, render_template, request
from ddtrace.runtime import RuntimeMetrics

RuntimeMetrics.enable()

app = Flask(__name__)
application = app

logger = logging.getLogger('curryware-front-end')
consoleOutputHandler = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consoleOutputHandler.setFormatter(formatter)
logger.addHandler(consoleOutputHandler)
logger.info('---curryware-front-end start---')


@app.route('/')
def index_page():
    logger.info('Launching app!')
    current_time = datetime.datetime.now()
    local_time = current_time.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
    user_agent = request.headers.get('User-Agent')
    logger.info('User agent: {}'.format(user_agent))
    current_date = '{}/{}/{}'.format(str(local_time.month), str(local_time.day), str(local_time.year),
                                     str(local_time.year))
    current_time = '{}:{}:{}'.format(str(local_time.hour), str(local_time.minute),
                                     str(local_time.second))

    log_environment_variable = os.environ.get('DD_LOGS_INJECTION')

    return render_template('index.html', title='Index Page', current_time=current_time,
                           current_date=current_date, user_agent=user_agent,
                           logs_injection_variable=log_environment_variable)


# if __name__ == '__main__':
#     app.run()

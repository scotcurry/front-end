import datetime
import logging

from flask import Flask, render_template, request

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
def hello_world():
    logger.info('Launching app!')
    current_time = datetime.datetime.now()
    user_agent = request.headers.get('User-Agent')
    logger.info('User agent: {}'.format(user_agent))
    current_time = (str(current_time.hour) + ':' + str(current_time.minute) + ':' +
                    str(current_time.second))
    return render_template('index.html', title='Index Page', current_time=current_time,
                           user_agent=user_agent)


# if __name__ == '__main__':
#     app.run()

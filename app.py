import datetime

from flask import Flask, render_template, request

app = Flask(__name__)
application = app


@app.route('/')
def hello_world():
    print('Launching app!')
    current_time = datetime.datetime.now()
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', title='Index Page', current_time=current_time,
                           user_agent=user_agent)


# if __name__ == '__main__':
#     app.run()

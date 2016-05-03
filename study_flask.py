from flask.ext.script import Manager
from flask import render_template
from flask import Flask
from flask import request
from flask.ext.bootstrap import Bootstrap

# from flask.ext.script import Manager
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/ip')
def ip():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
        return '<h1>Your X-Forwarded_For is %s </h1>' % ip
    else:
        ip = request.remote_addr
        remote_addr = request.remote_addr
        return '<h1>Your remote_addr is %s</p>' % remote_addr

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abc' #Dit zorgt voor een encryptie van de data cookies en sessie data, je kan dit ook gwn disablen als het problemen veroorzaakt
    return app

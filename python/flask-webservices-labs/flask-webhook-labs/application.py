from flask import Flask
from extensions import my_webhook

def some_function(request):
    do something

def some_other_function(request):
    do something else

def create_app():
    app = Flask(__name__)
    my_webhook.add_route('/something', methods=['GET', 'POST'])
    my_webhook.handlers['action1'] = some_function
    my_webhook.handlers['action2'] = some_other_function
    my_webhook.init_app(app)
    return app

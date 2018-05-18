from flask import Flask
from flask.ext.webhook import WebHook

app = Flask(__name__)

#create webhook object (name and app are optional)
#if app is not passed in in the constructor, my_webhook.init_app(app) is needed.
my_webhook = WebHook(name='optional_webhook_name', url_prefix='/webhooks' app=app)
my_webhook.add_route('/something', methods=['GET', 'POST'])

#define a function handler to be called by the webhook
def some_function(hookrequest):
  do something with the request object received by the webhook

#attach your function handler to the webhook.
#you can attach as many as you want and they all are going to be called
# () should not be included 
my_webhook.handlers['some_name_for_your_handler'] = some_function


# extensions.py
from flask.ext.webhook import WebHook

my_webhook = WebHook(url_prefix='/webhooks')


from flask import Flask, Blueprint
from flask.helpers import _endpoint_from_view_func
from quokka.core.config import QuokkaConfig
from quokka.utils.aliases import dispatch_aliases


class QuokkaApp(Flask):
    """
    Implementes customizations on Flask
    - Config handler
    - Aliases dispatching before request
    """

    config_class = QuokkaConfig

    def make_config(self, instance_relative=False):
        """This method should be removed when Flask is >=0.11"""
        root_path = self.root_path
        if instance_relative:
            root_path = self.instance_path
        return self.config_class(root_path, self.default_config)

    def preprocess_request(self):
        return dispatch_aliases() or super(QuokkaApp,
                                           self).preprocess_request()

    def add_quokka_url_rule(self, rule, endpoint=None,
                            view_func=None, **options):
        if endpoint is None:
            endpoint = _endpoint_from_view_func(view_func)
        if not endpoint.startswith('quokka.'):
            endpoint = 'quokka.core.' + endpoint
        self.add_url_rule(rule, endpoint, view_func, **options)


class QuokkaModule(Blueprint):
    "Overwrite blueprint namespace to quokka.modules.name"

    def __init__(self, name, *args, **kwargs):
        name = "quokka.modules." + name
        super(QuokkaModule, self).__init__(name, *args, **kwargs)

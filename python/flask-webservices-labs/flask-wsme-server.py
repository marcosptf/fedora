from wsme import WSRoot, expose

class MyService(WSRoot):
    @expose(unicode, unicode)  # First parameter is the return type,
                               # then the function argument types
    def hello(self, who=u'World'):
        return u"Hello {0} !".format(who)

ws = MyService(protocols=['restjson', 'restxml', 'soap'])
application = ws.wsgiapp()


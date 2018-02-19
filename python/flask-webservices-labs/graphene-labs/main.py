import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    hellos = graphene.String(name=graphene.String(default_value="stranger-hellos"))

    def resolve_hello(self, info, name):
        return 'Hello ' + name

    def resolve_hellos(self, info, name):
        return 'Hellos ' + name

schema = graphene.Schema(query=Query)

result = schema.execute('{ hello }')
print("result-hello===>>>")
print(result.data['hello'])

result = schema.execute('{ hellos }')
print("result-hellos===>>>")
print(result.data['hellos'])


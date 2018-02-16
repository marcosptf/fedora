####################################
#fazer os exemplos deste capitulo:
#http://docs.graphene-python.org/en/latest/types/
#
####################################
#importacao do componente graphene
import graphene

#esta classe eh responsavel por criar a query e schema do graphQL
class Query(graphene.ObjectType): #object do Graphene

    #o hello eh o nome da field
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    java = graphene.String(name=graphene.String(default_value="lang-java"))

    #funciona assim, def resolve_+nome-da-field
    def resolve_hello(self, info, name):
        return 'Hello ' + name

    def resolve_java(self, info, name):
        return 'def-call ' + name

#instancia o schema acima
schema = graphene.Schema(query=Query)

#executa o schema chamando pelo nome da field a ser executada
result = schema.execute('{ hello }')
print("result-hello===>>>")
print(result.data)
print(result.data['hello'])
print("\n")
result = schema.execute('{ java }')
print("result-def-java===>>>")
print(result.data['java'])


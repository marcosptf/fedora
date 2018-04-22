#http://docs.graphene-python.org/en/latest/execution/execute/
import graphene

#exemplo sem variaveis funcionando ===>>>
class User(graphene.ObjectType):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()

    def __init__(self, id, firstName, lastName):
        self.id = 12
        self.firstName = "java"
        self.lastName = "scripter"

class Query(graphene.ObjectType):
    user = graphene.Field(User)

    def resolve_user(self, info):
        return info.context['user']

schema = graphene.Schema(Query)
result = schema.execute(
    '''query getUser($id: ID) {
        user(id: $id) {
            id
            firstName
            lastName
        }
    }''',
    variable_values={'id': 12},
)

print("example=>9")
print("result real sample by doc oficial ====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n\n")

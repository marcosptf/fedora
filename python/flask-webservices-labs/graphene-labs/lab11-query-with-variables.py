import graphene

#exemplo3 com variaveis variaveis funcionando ===>>>
class User3(graphene.ObjectType):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()

    def __init__(self, id, firstName, lastName):
        self.id = 0
        self.firstName = "java"
        self.lastName = "scripter"

class Query_3(graphene.ObjectType):
    user = graphene.Field(User3)
    
    def resolve_user(self, info):
        return info.context.get('user')

schema = graphene.Schema(Query_3)

query_ql_2 = '''
        query getUser {
            user {
                id
                firstName
                lastName
            }
        }'''

result = schema.execute(query_ql_2, context_value={'user' : User3(id=1, firstName="java", lastName="scripter" )})
print("example=>3")
print("result-simple-query-with-variable-using return info.context.get('user') ====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n\n")



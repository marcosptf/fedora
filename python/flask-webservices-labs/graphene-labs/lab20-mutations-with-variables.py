import graphene

#exemplo2 com variaveis variaveis funcionando ===>>>
class User2(graphene.ObjectType):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()

    def __init__(self, id, firstName, lastName):
        #self.id = 0
        #self.firstName = "java-init"
        #self.lastName = "scripter-init"
        self.id = id
        self.firstName = firstName
        self.lastName = lastName

class Query_2(graphene.ObjectType):
    user = graphene.Field(User2)
    
    def resolve_user(self, info):
        return info.context.get('user')

schema = graphene.Schema(Query_2)

query_ql_2 = '''
        query getUser {
            user {
                id
                firstName
                lastName
            }
        }'''


#we need to create a mutation class to learn more how to it works
#...

result = schema.execute(query_ql_2, context_value={'user' : User2(id=1, firstName="java-ctx", lastName="scripter-ctx" )})
print("example=>2")
print("result-simple-query-with-variable-using return info.context.get('user') ====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n\n")


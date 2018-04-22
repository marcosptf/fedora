import graphene

#exemplo5 com variaveis variaveis funcionando ===>>>
class User5(graphene.ObjectType):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()

    def __init__(self, id, firstName, lastName):
        #variables
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        
        #hard-coding
        #self.id = 0
        #self.firstName = "python"
        #self.lastName = "python-3.6"

class Query_5(graphene.ObjectType):
    user = graphene.Field(User5)
    
    def resolve_user(self, info):
        return info.context.get('user')
        #return User4(id=0, firstName="fname", lastName="lname")

schema = graphene.Schema(Query_5)

query_ql_2 = '''
        query getUser {
            user {
                id
                firstName
                lastName
            }
        }'''

result = schema.execute(query_ql_2, context_value={'user' : User5(id=0, firstName="pylabs", lastName="py-labs3" )})
print("example=>5")
print("result-simple-query-with-variable-using using variables in queryQL ====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n\n")


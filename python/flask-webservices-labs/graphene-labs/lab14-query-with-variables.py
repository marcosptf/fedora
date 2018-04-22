import graphene

#exemplo6 com variaveis variaveis funcionando ===>>>
class User6(graphene.ObjectType):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()
    street = graphene.String()
    city = graphene.String()
    state = graphene.String()
    country = graphene.String()

    def __init__(self, id, firstName, lastName, street, city, state, country):
        #variables
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        
        #hard-coding
        #self.id = 0
        #self.firstName = "python"
        #self.lastName = "python-3.6"

class Query_6(graphene.ObjectType):
    user = graphene.Field(User6)
    
    def resolve_user(self, info):
        return info.context.get('user')
        #return User4(id=0, firstName="fname", lastName="lname")

schema = graphene.Schema(Query_6)

query_ql_2 = '''
        query getUser {
            user {
                street
                firstName
                lastName
                city
            }
        }'''

user_instance = User6(id=0, firstName="pylabs", lastName="py-labs3", street="st", city="ct", state="stt", country="ctry" )
result = schema.execute(query_ql_2, context_value={'user' : user_instance })
print("example=>6")
print("result-simple-query-with-variable-using using variables in queryQL ====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n\n")


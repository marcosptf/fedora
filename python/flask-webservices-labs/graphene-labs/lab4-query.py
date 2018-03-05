#http://docs.graphene-python.org/en/latest/execution/execute/
import graphene

"""
For executing a query a schema, you can directly call the execute method on it.
result represents the result of execution. 
result.data is the result of executing the query, 
result.errors is None if no errors occurred, and is a non-empty list if an error occurred.
schema = graphene.Schema(...)
result = schema.execute('{ name }')

Variables
You can pass variables to a query via variable_values.
"""

#pegar exemplo do lab5 para completar este ===>>>
class User(graphene.ObjectType):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()

class Query_0(graphene.ObjectType):
    user = graphene.Field(User)
    
    def resolve_user(self, info):
        #return info.context.get('user')
        return User(id=0, firstName="fname", lastName="lname")

schema = graphene.Schema(Query_0)
query_ql_0 = '''
       query getUser {
             user {
               id
               firstName
               lastName
            }
        }'''
result = schema.execute(query_ql_0)

print("result-simple-query-without-variable====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n")





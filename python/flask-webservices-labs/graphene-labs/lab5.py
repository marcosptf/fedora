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

    def __init__(self):
        self.user.id = 0
        self.user.firstName = "java"
        self.user.lastName = "scripter"


#example2 - variables
class Query_1(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.Int())
    
    def resolve_user(self, args, context, info):
        #self.user.id = 0
        #self.user.firstName = "java"
        #self.user.lastName = "scripter"
        
        query = User.get_query(context)
        
        print("debugger-field-user===>>>")
        print(info)
        print("debugger-info-context====>>>")
        print(info.context)
        print("debugger-info-context-getUser====>>>>")
        print(info.context.get(user))
        print("debugger-args====>>>>")
        print(args)
        print("debugger-context====>>>")
        print(context)
        print("debugger-query====>>>>")
        print(query)
     

        #return info.context.get(user)
        #return User(id=0, firstName="java", lastName="scripter")
        return query.get(args.get('id'))

schema = graphene.Schema(Query_1)
query_ql_1 = '''
       query getUser($id: ID) {
             user(id: $id) {
               id
               firstName
               lastName
            }
        }'''
query_ql_2 = '''
        user(id: $id) {
            id
            firstName
            lastName
        }
        '''
query_ql_3 = '''
        user(id: 0) {
            id
            firstName
            lastName
        }
        '''
query_ql_4 = '''
       query getUser($id: 0) {
             user(id: $id) {
               id
               firstName
               lastName
            }
        }'''
query_ql_5 = '''
       query getUser {
             user {
               id
               firstName
               lastName
            }
        }'''
query_ql_6 = '''
       query {
           user(id:0){
              id
              firstName
              lastName
           }
       }
         ''' 
#result = schema.execute(query_ql_1, variable_values={'id': 12, 'firstName': 'fname-query1', 'lastName':'flast-query1'},)
#result = schema.execute(query_ql_2, variable_values={'id': 0},)
result = schema.execute(query_ql_6)
print("debugger-schema====>>>")
print(schema)
print("result-query-with-variable-id====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-name====>>>>")
print(result.data['user'])
print("\n")








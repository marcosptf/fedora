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

#exemplo sem variaveis funcionando ===>>>
class User(graphene.ObjectType):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()

    def __init__(self, id, firstName, lastName):
        self.id = 0
        self.firstName = "java"
        self.lastName = "scripter"

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
print("example=>0")
print("result-simple-query-without-variable====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n\n")




#exemplo1 com variaveis variaveis funcionando ===>>>
class User1(graphene.ObjectType):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()

    def __init__(self, id, firstName, lastName):
        self.id = 0
        self.firstName = "java=>0"
        self.lastName = "scripter=>0"

class Query_1(graphene.ObjectType):
    user = graphene.Field(User1)
    
    def resolve_user(self, info):
        return info.context['user']

schema = graphene.Schema(Query_1)

query_ql_2 = '''
        query getUser {
            user {
                id
                firstName
                lastName
            }
        }'''

#when pass values in context_value is used this value
result = schema.execute(query_ql_2, context_value={'user' : User1(id=1, firstName="java=>1", lastName="scripter=>1" )})
print("example=>1")
print("result-simple-query-with-variable====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n\n")





#exemplo1 com variaveis variaveis funcionando ===>>>
class User2(graphene.ObjectType):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()

    def __init__(self, id, firstName, lastName):
        self.id = 2
        self.firstName = "java=>2"
        self.lastName = "scripter=>2"

class Query_2(graphene.ObjectType):
    user = graphene.Field(User2)
    
    def resolve_user(self, info):
        return info.context['user']

schema = graphene.Schema(Query_2)

query_ql_2 = '''
        query getUser {
            user {
                id
                firstName
                lastName
            }
        }'''

#when pass None to values, he use the self values defined in def __init__():
result = schema.execute(query_ql_2, context_value={'user' : User2(id=None, firstName=None, lastName=None)})
print("example=>2")
print("result-simple-query-with-variable====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n\n")





#exemplo1 com variaveis variaveis funcionando ===>>>
class User3(graphene.ObjectType):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()

    def __init__(self, id, firstName, lastName):
        self.id = 3
        self.firstName = "java=>3"
        self.lastName = "scripter=>3"

class Query_3(graphene.ObjectType):
    user = graphene.Field(
            User3, 
            id=graphene.Int(), 
            firstName=graphene.String(), 
            lastName=graphene.String()
        )
    
    #def resolve_user(self, info):
        #return info.context['user']

"""
we need to try this example:

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(Employee)
    all_roles = SQLAlchemyConnectionField(Role)
    role = relay.Node.Field(Role)

query Role($id: ID!){
  role(id: $id) {
    id
    name
  }
}

"""



    def resolve_user(self, args, context, info):
        query = User3.get_query(context)
        return query.get(args.get('id'))

schema = graphene.Schema(Query_3)

query_ql_2 = '''
        query getUser {
            user(id:'0') {
                id
                firstName
                lastName
            }
        }'''

#when pass None to values, he use the self values defined in def __init__():
#result = schema.execute(query_ql_2, context_value={'user' : User3(id=None, firstName=None, lastName=None)})
#result = schema.execute(query_ql_2, context_value={'user' : User3(id=id, firstName=firstName, lastName=lastName)})
result = schema.execute(query_ql_2)
print("example=>3")
print("result-simple-query-with-variable====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n\n")











#####################################################################
#####################################################################
##pegar exemplo do lab5 para completar este ===>>>
#class User(graphene.ObjectType):
    #id = graphene.ID()
    #firstName = graphene.String()
    #lastName = graphene.String()

    #def __init__(self):
        #self.user.id = 0
        #self.user.firstName = "java"
        #self.user.lastName = "scripter"


##example2 - variables
#class Query_1(graphene.ObjectType):
    ##user = graphene.Field(User, id=graphene.Int())
    #user = graphene.Field(User)    

    #def resolve_user(self):
        ##self.user.id = 0
        ##self.user.firstName = "java"
        ##self.user.lastName = "scripter"
        ##query = User.get_query(context)
        #return User(id=0, firstName="fname", lastName="lname")
        ##return User(0, "fname", "lname")    
    
        ##print("debugger-field-user===>>>")
        ##print(info)
        ##print("debugger-info-context====>>>")
        ##print(info.context)
        ##print("debugger-info-context-getUser====>>>>")
        ##print(info.context.get(user))
        ##print("debugger-args====>>>>")
        ##print(args)
        ##print("debugger-context====>>>")
        ##print(context)
        ##print("debugger-query====>>>>")
        ##print(query)
     

        ##return info.context.get(user)
        ##return User(id=0, firstName="java", lastName="scripter")
        ##return query.get(args.get('id'))
        ##return args

#schema = graphene.Schema(Query_1)
#query_ql_0 = '''
       #query getUser {
             #user {
               #id
               #firstName
               #lastName
            #}
        #}'''
       
#query_ql_1 = '''
       #query getUser($id: ID) {
             #user(id: $id) {
               #id
               #firstName
               #lastName
            #}
        #}'''
#query_ql_2 = '''
        #user(id: $id) {
            #id
            #firstName
            #lastName
        #}
        #'''
#query_ql_3 = '''
        #user(id: 0) {
            #id
            #firstName
            #lastName
        #}
        #'''
#query_ql_4 = '''
       #query getUser($id: 0) {
             #user(id: $id) {
               #id
               #firstName
               #lastName
            #}
        #}'''
#query_ql_5 = '''
       #query getUser {
             #user {
               #id
               #firstName
               #lastName
            #}
        #}'''
#query_ql_6 = '''
       #query {
           #user(id:0){
              #id
              #firstName
              #lastName
           #}
       #}
         #''' 
##result = schema.execute(query_ql_1, variable_values={'id': 12, 'firstName': 'fname-query1', 'lastName':'flast-query1'},)
##result = schema.execute(query_ql_2, variable_values={'id': 0},)
#result = schema.execute(query_ql_0)
#print("debugger-schema====>>>")
#print(schema)
#print("result-query-with-variable-id====>>>")
#print(result)
#print("result-data====>>>")
#print(result.data)
#print("result-data-name====>>>>")
#print(result.data['user'])
#print("\n")


##print("debugger-Query-object")
##q1 = Query_1()
##resolve_user





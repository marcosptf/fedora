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
        self.firstName = "java"
        self.lastName = "scripter"

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

result = schema.execute(query_ql_2, context_value={'user' : User1(id=1, firstName="java", lastName="scripter" )})
print("example=>1")
print("result-simple-query-with-variable====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n\n")






#exemplo2 com variaveis variaveis funcionando ===>>>
class User2(graphene.ObjectType):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()

    def __init__(self, id, firstName, lastName):
        self.id = 0
        self.firstName = "java"
        self.lastName = "scripter"

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

result = schema.execute(query_ql_2, context_value={'user' : User2(id=1, firstName="java", lastName="scripter" )})
print("example=>2")
print("result-simple-query-with-variable-using return info.context.get('user') ====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n\n")






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






#exemplo4 com variaveis variaveis funcionando ===>>>
class User4(graphene.ObjectType):
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()

    def __init__(self, id, firstName, lastName):
        #variables
        #self.id = id
        #self.firstName = firstName
        #self.lastName = lastName
        
        #hard-coding
        self.id = 0
        self.firstName = "python"
        self.lastName = "python-3.6"

class Query_4(graphene.ObjectType):
    user = graphene.Field(User4)
    
    def resolve_user(self, info):
        return info.context.get('user')
        #return User4(id=0, firstName="fname", lastName="lname")

schema = graphene.Schema(Query_4)

query_ql_2 = '''
        query getUser {
            user {
                id
                firstName
                lastName
            }
        }'''

result = schema.execute(query_ql_2, context_value={'user' : User4(id=None, firstName=None, lastName=None )})
print("example=>4")
print("result-simple-query-with-variable-using using variables in queryQL ====>>>")
print(result)
print("result-data====>>>")
print(result.data)
print("result-data-user====>>>>")
print(result.data['user'])
print("\n\n")






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






#exemplo7 com variaveis variaveis funcionando ===>>>
class User7(graphene.ObjectType):
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

class Query_7(graphene.ObjectType):
    user = graphene.Field(User6)
    
    def resolve_user(self, info):
        return info.context.get('user')
        #return User4(id=0, firstName="fname", lastName="lname")

schema = graphene.Schema(Query_7)

query_ql_2 = '''
        query getUser {
            user {
                street
                firstName
                lastName
                city
            }
        }'''


user_instance = User7(id=0, firstName="pylabs", lastName="py-labs3", street="st", city="ct", state="stt", country="ctry" )
result = schema.execute(query_ql_2, context_value={'user' : user_instance })
print("example=>7")
print("result-simple-query-with-variable-using using variables in queryQL ====>>>")
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





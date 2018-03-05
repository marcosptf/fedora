#http://docs.graphene-python.org/en/latest/execution/execute/
import graphene

"""
For executing a query a schema, you can directly call the execute method on it.
result represents the result of execution. 
result.data is the result of executing the query, 
result.errors is None if no errors occurred, and is a non-empty list if an error occurred.
schema = graphene.Schema(...)
result = schema.execute('{ name }')
"""

"""
context
You can pass context to a query via context_value.
"""
class Query(graphene.ObjectType):
    name = graphene.String()

    def resolve_name(self, info):
        return info.context.get('name')

schema = graphene.Schema(Query)
result = schema.execute('{ name }', context_value={'name': 'Syrus'})

"""
Variables
You can pass variables to a query via variable_values.
"""
class Query(graphene.ObjectType):
    user = graphene.Field(User)

    def resolve_user(self, info):
        return info.context.get('user')

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



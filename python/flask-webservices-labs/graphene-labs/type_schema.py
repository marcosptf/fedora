#http://docs.graphene-python.org/en/latest/types/schema/

"""
#schema
my_schema = Schema(
    query=MyRootQuery,
    mutation=MyRootMutation,
)


#Types
my_schema = Schema(
    query=MyRootQuery,
    types=[SomeExtraObjectType, ]
)

#Querying
my_schema.execute('{ lastName }')

#Auto CamelCase field names
class Person(graphene.ObjectType):
    last_name = graphene.String()
    other_name = graphene.String(name='_other_Name')
    
#====>>>>>   
{
    lastName
    _other_Name
}

#to disable CamelCase
my_schema = Schema(
    query=MyRootQuery,
    auto_camelcase=False,
)



"""
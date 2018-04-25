#http://docs.graphene-python.org/en/latest/types/mutations/
import graphene

#entity
class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()
    
    def __init__(self, name, age):
        self.name = name
        self.age  = age

#class Personas(graphene.ObjectType):
    #data    

class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(lambda: Person)

    def mutate(self, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)
        

#the Mutation Class
class MyMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()

#We must define a query for our schema
class Query(graphene.ObjectType):
    person = graphene.Field(Person)
    
    def resolve_person(self, info):
        print("debugger=>")
        print(info)
        return info.context.get('person')

schema = graphene.Schema(query=Query, mutation=MyMutations)
#schema = graphene.Schema(query=Query)

'''
#Executing the Mutation
mutation myFirstMutation {
    createPerson(name:"Peter") {
        person {
            name
        }
        ok
    }
}

#======>>>>>
{
    "createPerson": {
        "person" : {
            name: "Peter"
        },
        "ok": true
    }
}
'''

query = '''
query getPerson{
    person {
        age
        name
    }
}
'''

person_instance = {'person' : Person(name="debugger=>0", age=13) }
result = schema.execute(query, context_value=person_instance)
print("result-object====>>>>")
print(result)
print("result-data====>>>>")
print(result.data)



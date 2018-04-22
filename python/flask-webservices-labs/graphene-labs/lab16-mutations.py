#http://docs.graphene-python.org/en/latest/types/mutations/
import graphene

class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()

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

schema = graphene.Schema(query=Query, mutation=MyMutations)


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







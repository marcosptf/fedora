#http://docs.graphene-python.org/en/latest/types/interfaces/

import graphene

class Character(graphene.Interface):
    name = graphene.String()

# Human is a Character implementation
class Human(graphene.ObjectType):
    class Meta:
        interfaces = (Character, )

    born_in = graphene.String()

# Droid is a Character implementation
class Droid(graphene.ObjectType):
    class Meta:
        interfaces = (Character, )

    function = graphene.String()


""" schema ====>>>>
interface Character {
  name: String
}

type Droid implements Character {
  name: String
  function: String
}

type Human implements Character {
  name: String
  bornIn: String
}


"""

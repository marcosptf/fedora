#http://docs.graphene-python.org/en/latest/types/list-and-nonnull/

import graphene

class Character(graphene.ObjectType):
    name = graphene.NonNull(graphene.String)
    
class Character(graphene.ObjectType):
    name = graphene.String(required=True)

class Character(graphene.ObjectType):
    appears_in = graphene.List(graphene.String)

class Character(graphene.ObjectType):
    appears_in = graphene.List(graphene.NonNull(graphene.String))
    
    
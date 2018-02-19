#http://docs.graphene-python.org/en/latest/types/objecttypes/

import graphene

class Person(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()

    def resolve_full_name(self, info):
        return '{} {}'.format(self.first_name, self.last_name)
      
      
""" ===>>>  query example
import graphene

class Query(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String())

    def resolve_reverse(self, info, word):
        return word[::-1]


#Resolvers outside the class

import graphene

def reverse(root, info, word):
    return word[::-1]

class Query(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String(), resolver=reverse)
    

#Instances as data containers
peter = Person(first_name='Peter', last_name='Griffin')
peter.first_name # prints "Peter"
peter.last_name # prints "Griffin"

     
"""        
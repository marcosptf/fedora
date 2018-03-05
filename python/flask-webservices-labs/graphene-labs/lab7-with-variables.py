import graphene


class Patron(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()

class Query(graphene.ObjectType):
    patron = graphene.Field(Patron)

    def resolve_patron(self, info):
        return Patron(id=0, name='java', age=12)

schema = graphene.Schema(query=Query)
query = '''
    query something{
      patron {
        id
        name
        age
      }
    }
'''
query2 = '''
    query something($id:ID){
      patron(id:$id) {
        id
        name
      }
    }
'''

if __name__ == '__main__':
    result = schema.execute(query2, variable_values={'id': 0})
    print(result.data['patron'])

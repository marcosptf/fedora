import graphene

#class GeoInput with graphene InputObjectType, this class is to set or get latlng
class GeoInput(graphene.InputObjectType):
    #two properties required
    lat = graphene.Float(required=True)
    lng = graphene.Float(required=True)

    #another properties that return lat+lng
    @property
    def latlng(self):
        return "({},{})".format(self.lat, self.lng)

#Address ObjectType graphene with properties latlng string
class Address(graphene.ObjectType):
    latlng = graphene.String()

#query ObjectType graphene that has a properties address that use address class and GeoInput class required
class Query(graphene.ObjectType):
    address = graphene.Field(Address, geo=GeoInput(required=True))

    #execute address field given info and geo variables
    def resolve_address(self, info, geo):
        #this return set latlng  string to Address class
        return Address(latlng=geo.latlng)

#mutation graphene class 
class CreateAddress(graphene.Mutation):
    
    #another class inside CreateAddress class, maybe it is a property?
    #this name Arguments is not call any place!
    class Arguments:
        #properties geo type GeoInput required
        geo = GeoInput(required=True)

    #this is a instance from Address to Output?
    #this name Output is not call any place!
    Output = Address

    #method mutate that give info and geo
    def mutate(self, info, geo):
        #return class Address setting latlng to new value geo type GeoInput
        return Address(latlng=geo.latlng)

#class mutation type ObjectType
class Mutation(graphene.ObjectType):
    #use createAddress class to create new Address
    #maybe CreateAddress.Field() is call class Arguments from CreateAddress class?
    create_address = CreateAddress.Field()

#mutations querys
mutation = '''
    mutation addAddress{
      createAddress(geo: {lat:13.7, lng:27}) {
        latlng
      }
    }
'''

#query getting addres from some lat and lng
query = '''
    query something{
      address(geo: {lat:32.2, lng:12}) {
        latlng
      }
    }
'''

#instance from new schema to query and mutation
schema = graphene.Schema(query=Query, mutation=Mutation)


#def test_query():
    #result = schema.execute(query)
    #assert not result.errors
    #assert result.data == {
        #'address': {
            #'latlng': "(32.2,12.0)",
        #}
    #}


#def test_mutation():
    #result = schema.execute(mutation)
    #assert not result.errors
    #assert result.data == {
        #'createAddress': {
            #'latlng': "(13.7, 27.8)",
        #}
    #}


if __name__ == '__main__':
    print("starting app mutations example lab19==>>>")
    print("running query=>>")
    result = schema.execute(query)
    print("resp query====>>>")
    print(result.data['address']['latlng'])
    print("running mutation ===>>>")
    schema.execute(schema.execute(mutation))
    print("running query again===>>>")
    result = schema.execute(query)
    print("resp query 2 ===>>>>")
    print(result.data['address']['latlng'])



import graphene

result = None

#class GeoInput with graphene InputObjectType, this class is to set or get latlng
class GeoInput(graphene.InputObjectType):
    
    #two properties required
    lat = graphene.Float(required=False)
    lng = graphene.Float(required=False)

    #another properties that return lat+lng
    @property
    def latlng(self):
        print("def-latlng=>")
        print("lat==>"+self.lat)
        print("lng==>"+self.lng)
        if self.lat and self.lng:
            print("def-latlng-if")
            result = "({},{})".format(self.lat, self.lng)
        print("def-latlng-result=>"+result)    
        return result



#Address ObjectType graphene with properties latlng string
class Address(graphene.ObjectType):
    
    #properties used on queryQL to answer
    latlng = graphene.String()
 


#query ObjectType graphene that has a properties address that use address class and GeoInput class required
class Query(graphene.ObjectType):
    
    #this properties is used to perform queryQL, is required lat, lng parameters;
    address = graphene.Field(Address, geo=GeoInput(required=False))

    #execute address field given info and geo variables
    def resolve_address(self, info, geo):
        
        #this return set latlng  string to Address class
        #return Address(latlng=geo.latlng)
        print("debugger-geo.latlng====>>>")
        print(geo.latlng)
        if geo.latlng!="(None,None)":
            print("debugger->if")
            return Address(latlng=geo.latlng)
        print("debugger->None")
        add = Address()
        return add.resp()    



#mutation graphene class 
class CreateAddress(graphene.Mutation):
    
    #another class inside CreateAddress class, maybe it is a property?
    #this name Arguments is not call any place!
    class Arguments:

        #properties geo type GeoInput required
        geo = GeoInput(required=False)

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

query1 = '''
    query something{
      address(geo: {lat:44.7, lng:77}) {
        latlng
      }
    }
'''

query2 = '''
    query something{
      address(geo: {}) {
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


#if __name__ == '__main__':
print("starting app mutations example lab19==>>>")
print("running query=>>")
result = schema.execute(query1)
print("resp query====>>>")
print(result.data['address']['latlng'])
print("running mutation ===>>>")
schema.execute(schema.execute(mutation))
print("running query again===>>>")
result = schema.execute(query2)
print("resp query 2 ===>>>>")
print(result.data['address']['latlng'])



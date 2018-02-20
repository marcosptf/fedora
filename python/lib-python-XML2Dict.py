#pip install xml2dict

from encoder import XML2Dict
obj = XML2Dict("utf-8")
print(obj.parse("<person><name>spring</name><age></age><address /></person>"))
{'person': {'address': '', 'age': '', 'name': b'spring'}}

#example:
#http://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/

#new example/labs to do querys using relay and mutations
#imports
from flask import Flask
from flask_graphql import GraphQLView
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

#engine intance
engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)

#start session from sqlalchemy
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

#start Base query 
Base = declarative_base()
Base.query = db_session.query_property()

#models class
class DepartmentModel(Base):
    #table-name
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)

#models class
class EmployeeModel(Base):
    #table-name
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship(
        DepartmentModel,
        backref=backref('employees',
                        uselist=True,
                        cascade='delete,all'))

#class entity to do querys graphene
class Department(SQLAlchemyObjectType):
    class Meta:
        #this class represent DepartmentModel class
        model = DepartmentModel
        #implement interface relay.Node 
        interfaces = (relay.Node, )

#class entity to do querys graphene
class Employee(SQLAlchemyObjectType):
    class Meta:
        #this class represent EmployeeModel class
        model = EmployeeModel
        #implement interface relay.Node
        interfaces = (relay.Node, )

#class graphene to query using SQLAlchemy Entitys
class Query(graphene.ObjectType):
    
    """
    this property represent: Node Root field
    As is required in the Relay specification, the server must implement a root field called node that returns a Node Interface.
    For this reason, graphene provides the field relay.Node.Field, which links to any type in the Schema which implements Node.     
    """
    dados = relay.Node.Field()

    """
    this property represent querys graphql to entity Employe
    to do query to this property:
    {
        todosEmpregados {
                edges{
                    node{
                    id
                    name
                }
            }
        }
    }
    
    property name:       query graphQL
    todos_empregados =>  todosEmpregados {  }

    edges => its a node field that link one node field to another node field
    node => fields from entity EmployeeModel
    
    """
    todos_empregados = SQLAlchemyConnectionField(Employee)
    

    """
    this property represent querys graphql to entity Department
    to do query to this property:
    {
        todosDepart {
                edges{
                    node{
                    id
                    name
                }
            }
        }
    }
    
    property name:       query graphQL
    todos_depart =>  todosDepart {  }

    edges => its a node field that link one node field to another node field
    node => fields from entity DepartmentModel
    """
    todos_depart = SQLAlchemyConnectionField(Department)


#schema instance to do querys
schema = graphene.Schema(query=Query)

#we need to learn how to do mutations querys
#class Mutations()....





""" 
#studyes about relay:
https://facebook.github.io/relay/docs/en/quick-start-guide.html

escrever esta query
{
  allEmployees {
    edges {
      dados {
        id
        name
        department {
          name
        }
      }
    }
  }
}
"""






app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        #for having the GraphiQL interface
        graphiql=True 
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()

"""
. .venv/bin/activate
python3

>>> from models import engine, db_session, Base, Department, Employee
>>> Base.metadata.create_all(bind=engine)

>>> # Fill the tables with some data
>>> engineering = Department(name='Engineering')
>>> db_session.add(engineering)
>>> hr = Department(name='Human Resources')
>>> db_session.add(hr)

>>> peter = Employee(name='Peter', department=engineering)
>>> db_session.add(peter)
>>> roy = Employee(name='Roy', department=engineering)
>>> db_session.add(roy)
>>> tracy = Employee(name='Tracy', department=hr)
>>> db_session.add(tracy)
>>> db_session.commit()


$ (.venv) python3 ./app.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

#acessar:
http://localhost:5000/graphql

#escrever esta query
{
  allEmployees {
    edges {
      node {
        id
        name
        department {
          name
        }
      }
    }
  }
}

#response-graphql:
{
  "data": {
    "allEmployees": {
      "edges": [
        {
          "node": {
            "id": "RW1wbG95ZWU6MQ==",
            "name": "Peter",
            "department": {
              "name": "Engineering"
            }
          }
        },
        {
          "node": {
            "id": "RW1wbG95ZWU6Mg==",
            "name": "Roy",
            "department": {
              "name": "Engineering"
            }
          }
        },
        {
          "node": {
            "id": "RW1wbG95ZWU6Mw==",
            "name": "Tracy",
            "department": {
              "name": "Human Resources"
            }
          }
        }
      ]
    }
  }
}


#fazer este exemplos de querys
http://docs.graphene-python.org/projects/sqlalchemy/en/latest/tips/

#schema examples
http://docs.graphene-python.org/projects/sqlalchemy/en/latest/examples/

#criar classes de mutations com estes examples
http://docs.graphene-python.org/en/latest/types/mutations/




#anatomia de uma query
{
  
  allEmployees {
		edges{
      node{
        id
        name
      }
    }
  }
}





"""



















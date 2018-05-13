import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Department as DepartmentModel, Employee as EmployeeModel

class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )

class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    dados = relay.Node.Field()
    todos_empregados = SQLAlchemyConnectionField(Employee)
    todos_depart = SQLAlchemyConnectionField(Department)

schema = graphene.Schema(query=Query)

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

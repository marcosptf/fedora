#example:
#http://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/
#
from flask import Flask
from flask_graphql import GraphQLView

from models import db_session
from schema import schema, Department

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
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



















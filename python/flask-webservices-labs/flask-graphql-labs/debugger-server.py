"""
https://travis-ci.org/graphql-python/flask-graphql/jobs/326153616

#rodar testes no python 2.7
export TOX_ENV=py27
tox -e $TOX_ENV -- --cov=flask_graphql
tox -e py27 -- --cov=flask_graphql
tox -e python -- --cov=flask_graphql
py.test tests --cov=flask_graphql

#rodar testes no python 3.6
export TOX_ENV=py36,import-order,flake8
source ~/virtualenv/python3.6/bin/activate
tox -e $TOX_ENV -- --cov=flask_graphql
py.test tests --cov=flask_graphql

"""
from flask import Flask
from flask_graphql import GraphQLView
from graphql.type.definition import GraphQLArgument, GraphQLField, GraphQLNonNull, GraphQLObjectType
from graphql.type.scalars import GraphQLString
from graphql.type.schema import GraphQLSchema


def resolve_raises(*_):
    raise Exception("Throws!")



#query{
  #perl
#}

QueryRootType = GraphQLObjectType(
    name='java',
    #fields={
        #'thrower': GraphQLField(GraphQLNonNull(GraphQLString), resolver=resolve_raises),
        #'request': GraphQLField(GraphQLNonNull(GraphQLString),
                                #resolver=lambda obj, args, context, info: context.args.get('q')),
        #'context': GraphQLField(GraphQLNonNull(GraphQLString),
                               #resolver=lambda obj, args, context, info: context),
        #'test': GraphQLField(
            #type=GraphQLString,
            #args={
                #'who': GraphQLArgument(GraphQLString)
            #},
            #resolver=lambda obj, args, context, info: 'Hello %s' % (args.get('who') or 'World')
            ##resolver=lambda args, info: 'debugger=> %s' % (args.get("who"))
        #)
    #}
    
    fields={
        'perl': GraphQLField(GraphQLString),
    }    
    
)

MutationRootType = GraphQLObjectType(
    name='MutationRoot',
    fields={
        'writeTest': GraphQLField(
            type=QueryRootType,
            resolver=lambda *_: QueryRootType
        )
    }
)
Schema = GraphQLSchema(QueryRootType, MutationRootType)

def create_app(path='/graphql', **kwargs):
    app = Flask(__name__)
    app.debug = True
    app.add_url_rule(path, view_func=GraphQLView.as_view('graphql', schema=Schema, graphiql=True))
    return app


if __name__ == '__main__':
    app = create_app(graphiql=True)
    app.run()














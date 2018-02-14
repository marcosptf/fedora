from flask import Flask
from flask_graphql import GraphQLView
from graphql.type.definition import GraphQLArgument, GraphQLField, GraphQLNonNull, GraphQLObjectType
from graphql.type.scalars import GraphQLString
from graphql.type.schema import GraphQLSchema


def resolve_raises(*_):
    raise Exception("Throws!")


QueryRootType = GraphQLObjectType(
    name='QueryRoot',
    fields={
        #'thrower': GraphQLField(GraphQLNonNull(GraphQLString), resolver=resolve_raises),
        #'request': GraphQLField(GraphQLNonNull(GraphQLString),
        #                        resolver=lambda obj, args, context, info: context.args.get('q')),
        #'context': GraphQLField(GraphQLNonNull(GraphQLString),
        #                        resolver=lambda obj, args, context, info: context),
        'test': GraphQLField(
            type=GraphQLString,
            args={
                'who': GraphQLArgument(GraphQLString)
            },
            #resolver=lambda obj, args, context, info: 'Hello %s' % (args.get('who') or 'World')
            resolver=lambda args, info: 'debugger=> %s' % (args.get("who"))
        )
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
    app.add_url_rule(path, view_func=GraphQLView.as_view('graphql', schema=Schema, **kwargs))
    return app


if __name__ == '__main__':
    app = create_app(graphiql=True)
    app.run()














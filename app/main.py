from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema

from app.gql.query import Query
from app.repository.mission_repository import get_missions_in_date_range

app = Flask(__name__)
schema = Schema(query=Query)
app.add_url_rule(
   '/graphql',
   view_func=GraphQLView.as_view(
       'graphql',
       schema=schema,
       graphiql=True
   )
)

if __name__ == "__main__":
    app.run()

"""
The api blueprint.
"""

from flask import Blueprint
from flask_graphql import GraphQLView  # type: ignore

from adeline.persistence.schema import schema

api = Blueprint("api", __name__)

api.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

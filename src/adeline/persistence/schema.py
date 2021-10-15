"""
Persistence schemas
"""

from graphene import ObjectType, Schema, relay
from graphene_sqlalchemy import (  # type: ignore
    SQLAlchemyConnectionField,
    SQLAlchemyObjectType,
)

from adeline.persistence.models import Group as GroupModel
from adeline.persistence.models import Person as PersonModel


class Group(SQLAlchemyObjectType):
    """
    A group of Persons
    """

    class Meta:
        """
        Group metaclass
        """

        model = GroupModel
        interfaces = (relay.Node,)


class Person(SQLAlchemyObjectType):
    """
    A person who uses the webapp
    """

    class Meta:
        """
        Person metaclass
        """

        model = PersonModel
        interfaces = (relay.Node,)


class Query(ObjectType):
    """
    GraphQL query class
    """

    node = relay.Node.Field()

    # Allows sorting over multiple columns, by default over the primary key
    all_persons = SQLAlchemyConnectionField(Person.connection)

    # Disable sorting over this field
    all_groups = SQLAlchemyConnectionField(Group.connection, sort=None)


schema: Schema = Schema(query=Query)

import graphene
from graphql_jwt.decorators import login_required
from graphene_django import DjangoObjectType

from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name",
                  "last_name", "is_staff", "is_active",
                  "date_of_birth")


class UserQuery(graphene.ObjectType):
    user = graphene.Field(UserType, token=graphene.String(required=True))

    @login_required
    def resolve_user(self, info, **kwargs):
        return info.context.user


class UserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):

        user = User(username=kwargs['username'])
        user.set_password(kwargs['password'])

        user.save()

        return UserMutation(user=user)
from graphene import Mutation, Boolean, Field, Int
from app.repository.target_repository import add_new_target
from app.gql.tyeps.target_type import TargetInputType, TargetType

class AddTarget(Mutation):
    class Arguments:
        target_data = TargetInputType(required=True)

    ok = Boolean()
    target = Field(TargetType)

    @staticmethod
    def mutate(root, info, target_data):
        new_target = add_new_target(target_data)
        return AddTarget(target=new_target, ok=True)

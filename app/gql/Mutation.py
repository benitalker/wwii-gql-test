from graphene import ObjectType
from app.gql.mutations.mission_mutations import AddMission, UpdateMission, DeleteMission
from app.gql.mutations.target_mutations import AddTarget

class Mutation(ObjectType):
    add_new_mission = AddMission.Field()
    add_new_target = AddTarget.Field()
    update_mission = UpdateMission.Field()
    # delete_mission = DeleteMission.Field()

from graphene import ObjectType, List, Field, Int

from app.gql.tyeps import MissionType
from app.repository.mission_repository import get_all_missions, get_mission_by_id


class Query(ObjectType):
    get_all_missions = List(MissionType)
    get_mission_by_id = Field(MissionType,mission_id=Int(required=True))


    @staticmethod
    def resolve_get_all_missions(root, info):
       return get_all_missions()

    @staticmethod
    def resolve_get_mission_by_id(root,info,mission_id):
        return get_mission_by_id(mission_id)

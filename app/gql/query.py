from graphene import ObjectType, List, Field, Int, Date, String

from app.gql.tyeps import MissionType
from app.repository.mission_repository import get_all_missions, get_mission_by_id, get_missions_in_date_range, \
    get_missions_by_county_name


class Query(ObjectType):
    get_all_missions = List(MissionType)
    get_mission_by_id = Field(MissionType,mission_id=Int(required=True))
    get_missions_in_date_range = List(MissionType,start_date=Date(required=True),end_date=Date(required=True))
    get_missions_by_county_name = List(MissionType,country_name=String(required=True))

    @staticmethod
    def resolve_get_all_missions(root, info):
       return get_all_missions()

    @staticmethod
    def resolve_get_mission_by_id(root,info,mission_id):
        return get_mission_by_id(mission_id)

    @staticmethod
    def resolve_get_missions_in_date_range(root,info,start_date,end_date):
        return get_missions_in_date_range(start_date,end_date)

    @staticmethod
    def resolve_get_missions_by_county_name(root,info,country_name):
        return get_missions_by_county_name(country_name)

from dataclasses import field

from graphene import ObjectType, List, Field, Int, Date, String

from app.gql.tyeps import MissionType, LimitedMissionType
from app.gql.tyeps.mission_statistic_type import MissionStatisticsType
from app.repository.mission_repository import get_all_missions, get_mission_by_id, get_missions_in_date_range, \
    get_missions_by_county_name, get_missions_by_target_industry, get_missions_by_target_type, \
    get_mission_statistics_for_city


class Query(ObjectType):
    get_all_missions = List(MissionType)
    get_mission_by_id = Field(MissionType,mission_id=Int(required=True))
    get_missions_in_date_range = List(MissionType,start_date=Date(required=True),end_date=Date(required=True))
    get_missions_by_county_name = List(MissionType,country_name=String(required=True))
    get_missions_by_target_industry = List(MissionType,target_industry=String(required=True))
    get_missions_by_target_type = List(LimitedMissionType,target_type=String(required=True))
    get_mission_statistics_for_city = Field(MissionStatisticsType, city_name=String(required=True))

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

    @staticmethod
    def resolve_get_missions_by_target_industry(root,info,target_industry):
        return get_missions_by_target_industry(target_industry)

    @staticmethod
    def resolve_get_missions_by_target_type(root,info,target_type):
        return get_missions_by_target_type(target_type)

    @staticmethod
    def resolve_get_mission_statistics_for_city(root,info,city_name):
        return get_mission_statistics_for_city(city_name)

from graphene import ObjectType, List, Int, Float, String
from app.gql.tyeps import MissionType

class MissionStatisticsType(ObjectType):
    missions = List(MissionType)
    total_missions = Int()
    average_target_priority = Float()
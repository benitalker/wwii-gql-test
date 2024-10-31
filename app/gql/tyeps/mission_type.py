from graphene import ObjectType, Int, InputObjectType
from graphene.types.datetime import Date

class MissionType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Int()
    attacking_aircraft = Int()
    bombing_aircraft = Int()
    aircraft_returned = Int()
    aircraft_failed = Int()
    aircraft_damaged = Int()
    aircraft_lost = Int()

class MissionInputType(InputObjectType):
    mission_id = Int()
    mission_date = Date(default_value=None)
    airborne_aircraft = Int(default_value=None)
    attacking_aircraft = Int(default_value=None)
    bombing_aircraft = Int(default_value=None)
    aircraft_returned = Int(default_value=None)
    aircraft_failed = Int(default_value=None)
    aircraft_damaged = Int(default_value=None)
    aircraft_lost = Int(default_value=None)

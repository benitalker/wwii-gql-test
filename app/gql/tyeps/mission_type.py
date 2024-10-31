from graphene import ObjectType, Int, Date, String

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

from graphene import ObjectType, Int

class LimitedMissionType(ObjectType):
    returned_aircraft = Int()
    failed_aircraft = Int()
    damaged_aircraft = Int()
    lost_aircraft = Int()


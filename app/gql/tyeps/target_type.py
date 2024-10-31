from graphene import ObjectType, Int, String, InputObjectType

class TargetType(ObjectType):
    target_id = Int()
    mission_id = Int()
    target_industry = String()
    city_id = Int()
    target_type_id = Int()
    target_priority = Int()

class TargetInputType(InputObjectType):
    target_id = Int()
    mission_id = Int()
    target_industry = String(default_value=None)
    city_id = Int()
    target_type_id = Int()
    target_priority = Int(default_value=None)

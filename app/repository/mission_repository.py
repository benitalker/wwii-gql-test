from typing import List
from app.db.database import session_maker
from app.db.models import Mission, Target, City, Country, TargetType
from sqlalchemy import func

def get_all_missions() -> List[Mission]:
    with session_maker() as session:
        return session.query(Mission).all()

def get_mission_by_id(mission_id) -> Mission:
    with session_maker() as session:
        mission =  session.query(Mission).filter(Mission.mission_id == mission_id).first()
        if not mission:
            raise Exception("Mission result not found")
        return mission

def get_missions_in_date_range(start_date,end_date) -> List[Mission]:
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_date.between(start_date, end_date)).all()

def get_missions_by_county_name(country_name):
    with session_maker() as session:
        return (session.query(Mission)
        .join(Mission.targets)
        .join(Target.city)
        .join(City.country).filter(Country.country_name == country_name).all())

def get_missions_by_target_industry(target_industry):
    with session_maker() as session:
        return (session.query(Mission)
        .join(Mission.targets)
        .filter(Target.target_industry == target_industry).all())

def get_missions_by_target_type(target_type):
    with session_maker() as session:
        return (session.query(Mission)
                .join(Mission.targets)
                .join(Target.target_type)
                .filter(TargetType.target_type_name == target_type).all())

def add_new_mission(mission_data):
    with session_maker() as session:
        new_mission = Mission(**mission_data)
        session.add(new_mission)
        session.commit()
        return mission_data

def update_mission_by_id(mission_id, attack_result_data):
    with session_maker() as session:
        attack_result = session.query(Mission).filter_by(mission_id=mission_id).first()
        if not attack_result:
            raise Exception("Mission result not found")

        for key, value in attack_result_data.items():
            setattr(attack_result, key, value)

        session.commit()
        session.refresh(attack_result)
        return attack_result

def delete_mission(mission_id):
    with session_maker() as session:
        mission = session.query(Mission).filter_by(mission_id=mission_id).first()
        if not mission:
            raise Exception("Mission not found")

        session.query(Target).filter_by(mission_id=mission_id).delete()
        session.query(Mission).filter_by(mission_id=mission_id).delete()

        session.delete(mission)
        session.commit()


from sqlalchemy.sql import func


def get_mission_statistics_for_city(city_name):
    with session_maker() as session:
        city_stat_query = (session.query(Mission)
                           .join(Mission.targets)
                           .join(Target.city)
                           .filter(City.city_name == city_name))

        city_stat = city_stat_query.all()

        if not city_stat:
            raise ValueError(f"No statistics found for city: {city_name}")

        total_missions = len(city_stat)

        avg_priority_query = (session.query(func.avg(Target.target_priority))
                              .join(Mission)
                              .join(City)
                              .filter(City.city_name == city_name)
                              .scalar())

        return {
            'missions': city_stat,
            'total_missions': total_missions,
            'average_target_priority': avg_priority_query
        }

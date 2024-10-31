from typing import List
from sqlalchemy import func
from app.db.database import session_maker
from app.db.models import Mission, Target, City, Country


def get_all_missions() -> List[Mission]:
    with session_maker() as session:
        return session.query(Mission).all()

def get_mission_by_id(mission_id) -> Mission:
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_id == mission_id).first()

def get_missions_in_date_range(start_date,end_date) -> List[Mission]:
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_date.between(start_date, end_date)).all()

# def get_missions_by_county_name(country_name):
#     with session_maker() as session:
#         return session.query(Mission).join(Mission.targets).join(Target.city).join(City.country).filter(Country.country_name == country_name).all()

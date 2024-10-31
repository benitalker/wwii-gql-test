from typing import List
from app.db.database import session_maker
from app.db.models import Mission

def get_all_missions() -> List[Mission]:
    with session_maker() as session:
        return session.query(Mission).all()

def get_mission_by_id(mission_id) -> Mission:
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_id == mission_id).first()
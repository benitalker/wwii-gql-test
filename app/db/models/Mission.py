from sqlalchemy import Column, Integer, Date, String

from app.db.database import Base


class Mission(Base):
    __tablename__ = "mission"

    mission_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_date = Column(Date, nullable=False)
    theater_of_operations = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    air_force = Column(String(100), nullable=False)
    unit_id = Column(String(100), nullable=False)
    mission_type = Column(String(100), nullable=False)
    takeoff_base = Column(String(255), nullable=False)
    takeoff_location = Column(String(255))
    attacking_aircraft = Column(Integer)
    bombing_aircraft = Column(Integer)
    aircraft_returned = Column(Integer)
    aircraft_failed = Column(Integer)

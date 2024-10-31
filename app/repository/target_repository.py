from app.db.database import session_maker
from app.db.models import Target

def add_new_target(target_data):

    with session_maker() as session:
        new_target = Target(**target_data)
        session.add(new_target)
        session.commit()
        return target_data

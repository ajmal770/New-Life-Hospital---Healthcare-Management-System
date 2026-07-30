import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Doctor

app = create_app()

def seed_database():
    with app.app_context():
        # Check if doctors already exist
        if Doctor.query.first() is None:
            doctors = [
                Doctor(name='Dr John Smith', specialization='Cardiology'),
                Doctor(name='Dr Emma Wilson', specialization='Neurology'),
                Doctor(name='Dr David Brown', specialization='Orthopedics')
            ]
            
            db.session.bulk_save_objects(doctors)
            db.session.commit()
            print("Database seeded with default doctors.")
        else:
            print("Database already contains doctor records. Seeding skipped.")

if __name__ == '__main__':
    seed_database()

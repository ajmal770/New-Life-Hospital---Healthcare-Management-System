from app import create_app, db
from app.models import Doctor

app = create_app()

with app.app_context():
    new_doctor = Doctor(name="Dr. Olivia Benson", specialization="Oncology")
    db.session.add(new_doctor)
    db.session.commit()
    print("Added new doctors successfully.")

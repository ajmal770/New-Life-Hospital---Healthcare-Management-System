from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length, Regexp
from datetime import date
from app.models import Doctor

class BookingForm(FlaskForm):
    patient_name = StringField('Patient Name', validators=[
        DataRequired(message="Patient name is required."),
        Length(min=2, max=150, message="Patient name must be between 2 and 150 characters."),
        Regexp(r'^[a-zA-Z\s\-\'\.]+$', message="Patient name can only contain letters, spaces, hyphens, apostrophes, and periods.")
    ])
    doctor_id = SelectField('Doctor', coerce=int, validators=[DataRequired(message="Please select a doctor.")])
    appointment_date = DateField('Appointment Date', validators=[DataRequired(message="Date is required.")])
    time_slot = SelectField('Time Slot', validators=[DataRequired(message="Please select a time slot.")])
    submit = SubmitField('Book Appointment')

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.doctor_id.choices = [(d.id, f"{d.name} - {d.specialization}") for d in Doctor.query.all()]

    def validate_appointment_date(self, field):
        if field.data and field.data < date.today():
            raise ValidationError("Appointment date must be in the future.")
    
    def validate_doctor_id(self, field):
        if field.data:
            doctor = Doctor.query.get(field.data)
            if not doctor:
                raise ValidationError("Invalid doctor selected.")

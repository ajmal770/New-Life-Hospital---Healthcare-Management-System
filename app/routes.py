from flask import render_template, redirect, url_for, flash, request, current_app
from app import db
from app.models import Doctor, Appointment
from app.forms import BookingForm
from app.utils import generate_time_slots
from datetime import date
from sqlalchemy import exc

def register_routes(app):


    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/booking', methods=['GET', 'POST'])
    def booking():
        try:
            form = BookingForm()
            form.time_slot.choices = generate_time_slots()
            
            recent_appointments = Appointment.query.order_by(Appointment.created_at.desc()).limit(5).all()

            if form.validate_on_submit():
                patient_name = form.patient_name.data.strip()
                doctor_id = form.doctor_id.data
                appointment_date = form.appointment_date.data
                time_slot = form.time_slot.data
                
                # Validate doctor exists
                doctor = Doctor.query.get(doctor_id)
                if not doctor:
                    flash("Invalid doctor selected. Please try again.", "error")
                    return render_template('booking.html', form=form, recent_appointments=recent_appointments)
                
                # Check for duplicate appointment (double-booking prevention)
                existing = Appointment.query.filter_by(
                    doctor_id=doctor_id,
                    appointment_date=appointment_date,
                    time_slot=time_slot
                ).first()

                if existing:
                    db.session.rollback()
                    flash(f"Error: {doctor.name} is already booked at {time_slot} on {appointment_date.strftime('%Y-%m-%d')}.", "error")
                else:
                    try:
                        new_appointment = Appointment(
                            doctor_id=doctor_id,
                            patient_name=patient_name,
                            appointment_date=appointment_date,
                            time_slot=time_slot
                        )
                        db.session.add(new_appointment)
                        db.session.commit()
                        flash("Appointment booked successfully.", "success")
                        return redirect(url_for('booking'))
                    except exc.SQLAlchemyError as e:
                        db.session.rollback()
                        current_app.logger.error(f"Database error during booking: {str(e)}")
                        flash("An error occurred while booking. Please try again.", "error")
            elif request.method == 'POST':
                 flash("Please complete all fields correctly.", "warning")

            return render_template('booking.html', form=form, recent_appointments=recent_appointments)
        except Exception as e:
            current_app.logger.error(f"Unexpected error in booking route: {str(e)}")
            flash("An unexpected error occurred. Please try again.", "error")
            return render_template('booking.html', form=form, recent_appointments=recent_appointments)

    @app.route('/doctors')
    def doctors_list():
        doctors = Doctor.query.all()
        return render_template('doctors.html', doctors=doctors)

    @app.route('/departments')
    def departments():
        return render_template('departments.html')

    @app.route('/doctor/<int:doctor_id>')
    def doctor_schedule(doctor_id):
        try:
            doctor = Doctor.query.get_or_404(doctor_id)
            all_doctors = Doctor.query.all()
            appointments = Appointment.query.filter_by(doctor_id=doctor_id).order_by(Appointment.appointment_date.asc(), Appointment.time_slot.asc()).all()
            return render_template('doctor_schedule.html', doctor=doctor, appointments=appointments, all_doctors=all_doctors)
        except Exception as e:
            current_app.logger.error(f"Error fetching doctor schedule: {str(e)}")
            flash("An error occurred while loading the doctor's schedule.", "error")
            return redirect(url_for('doctors_list'))

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

# In __init__.py we do: from app import routes; routes.register_routes(app)
# Need to update __init__.py to call this function.

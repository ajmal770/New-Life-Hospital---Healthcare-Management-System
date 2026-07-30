from datetime import datetime, timedelta

def generate_time_slots():
    """Generates 30-minute interval time slots from 09:00 AM to 05:00 PM."""
    slots = []
    start_time = datetime.strptime('09:00 AM', '%I:%M %p')
    end_time = datetime.strptime('05:00 PM', '%I:%M %p')
    
    current_time = start_time
    while current_time <= end_time:
        slots.append((current_time.strftime('%I:%M %p'), current_time.strftime('%I:%M %p')))
        current_time += timedelta(minutes=30)
        
    return slots

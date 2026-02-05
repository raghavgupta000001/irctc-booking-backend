import uuid

BOOKINGS = {}

def create_booking(data):
    booking_id = str(uuid.uuid4())
    BOOKINGS[booking_id] = {
        "status": "QUEUED",
        "data": data
    }
    return booking_id

def get_booking(booking_id):
    return BOOKINGS.get(booking_id)

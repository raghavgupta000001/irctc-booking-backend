import uuid
from collections import deque

QUEUE = deque()
BOOKINGS = {}
ACTIVE_BOOKING = None

def create_booking(data):
    booking_id = str(uuid.uuid4())

    BOOKINGS[booking_id] = {
        "status": "QUEUED",
        "data": data
    }

    QUEUE.append(booking_id)
    return booking_id

def get_booking(booking_id):
    return BOOKINGS.get(booking_id)

def get_queue_position(booking_id):
    if booking_id == ACTIVE_BOOKING:
        return 0
    try:
        return list(QUEUE).index(booking_id) + 1
    except ValueError:
        return -1

def start_next_booking():
    global ACTIVE_BOOKING

    if ACTIVE_BOOKING is not None:
        return None

    if not QUEUE:
        return None

    booking_id = QUEUE.popleft()
    BOOKINGS[booking_id]["status"] = "RUNNING"
    ACTIVE_BOOKING = booking_id
    return booking_id

def complete_booking(booking_id):
    global ACTIVE_BOOKING

    BOOKINGS[booking_id]["status"] = "COMPLETED"
    ACTIVE_BOOKING = None

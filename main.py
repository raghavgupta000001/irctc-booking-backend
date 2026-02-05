from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import BookingRequest
from storage import start_next_booking, get_booking
@app.post("/agent/complete/{booking_id}")
def agent_complete(booking_id: str):
    complete_booking(booking_id)
    return {"message": "Booking marked as completed"}

@app.post("/agent/get-next")
def agent_get_next():
    booking_id = start_next_booking()
    if not booking_id:
        return {"job": None}

    booking = get_booking(booking_id)
    return {
        "job": {
            "booking_id": booking_id,
            "data": booking["data"]
        }
    }

from storage import (
    create_booking,
    get_booking,
    get_queue_position,
    start_next_booking,
    complete_booking,
    ACTIVE_BOOKING
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit-booking")
def submit_booking(data: BookingRequest):
    booking_id = create_booking(data.dict())
    return {
        "booking_id": booking_id,
        "status": "QUEUED"
    }

@app.get("/booking-status/{booking_id}")
def booking_status(booking_id: str):
    booking = get_booking(booking_id)
    if not booking:
        return {"error": "Invalid booking ID"}

    return {
        "status": booking["status"],
        "queue_position": get_queue_position(booking_id)
    }

# ⚠️ TEMP: simulate execution
@app.post("/admin/start-next")
def admin_start_next():
    booking_id = start_next_booking()
    if not booking_id:
        return {"message": "No booking started"}
    return {"message": f"Booking {booking_id} started"}

@app.post("/admin/complete/{booking_id}")
def admin_complete(booking_id: str):
    complete_booking(booking_id)
    return {"message": f"Booking {booking_id} completed"}

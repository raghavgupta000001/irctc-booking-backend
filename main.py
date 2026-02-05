from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import BookingRequest
from storage import create_booking, get_booking

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict
    allow_credentials=True,
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
    return booking

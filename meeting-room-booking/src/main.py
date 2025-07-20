from datetime import datetime
from src.models.booking import Booking
from src.repositories.booking_repository import BookingRepository
from src.services.booking_service import BookingService
from src.patterns.factory import UserFactory, RoomFactory

def main():
    repo = BookingRepository()
    service = BookingService(repo)

    alice = UserFactory.create_user("Alice")
    salaA = RoomFactory.create_room("Sala A", 5)

    start = datetime(2025, 7, 21, 9, 0)
    end = datetime(2025, 7, 21, 10, 0)
    service.create_booking(alice, salaA, start, end)

    print("Reservas de Alice:")
    for b in service.get_bookings_by_user(alice.id):
        print(f"{b.user.name} reservó {b.room.name} de {b.start_time} a {b.end_time}")

if __name__ == "__main__":
    main()

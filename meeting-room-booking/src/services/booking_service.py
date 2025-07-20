from src.models.booking import Booking

class BookingService:
    def __init__(self, booking_repo):
        self.booking_repo = booking_repo

    def create_booking(self, user, room, start_time, end_time):
        for b in self.booking_repo.get_all():
            if b.room.id == room.id and not (end_time <= b.start_time or start_time >= b.end_time):
                raise Exception("Sala ocupada.")
        new_booking = Booking(user, room, start_time, end_time)
        self.booking_repo.add(new_booking)
        return new_booking

    def get_bookings_by_user(self, user_id):
        return [b for b in self.booking_repo.get_all() if b.user.id == user_id]

    def get_bookings_by_room(self, room_id):
        return [b for b in self.booking_repo.get_all() if b.room.id == room_id]

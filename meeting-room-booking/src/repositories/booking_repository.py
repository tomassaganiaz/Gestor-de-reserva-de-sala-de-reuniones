class BookingRepository:
    def __init__(self):
        self._bookings = []

    def add(self, booking):
        self._bookings.append(booking)

    def get_all(self):
        return self._bookings

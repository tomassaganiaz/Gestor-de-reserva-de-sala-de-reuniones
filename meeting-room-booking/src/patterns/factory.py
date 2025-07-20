from src.models.user import User
from src.models.room import Room

class UserFactory:
    _id = 1
    @classmethod
    def create_user(cls, name):
        user = User(cls._id, name)
        cls._id += 1
        return user

class RoomFactory:
    _id = 1
    @classmethod
    def create_room(cls, name, capacity):
        room = Room(cls._id, name, capacity)
        cls._id += 1
        return room

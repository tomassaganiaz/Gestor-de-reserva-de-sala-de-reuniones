class Room:
    def __init__(self, room_id: int, name: str, capacity: int):
        self.__id = room_id
        self.__name = name
        self.__capacity = capacity

    @property
    def id(self): return self.__id
    @property
    def name(self): return self.__name
    @property
    def capacity(self): return self.__capacity

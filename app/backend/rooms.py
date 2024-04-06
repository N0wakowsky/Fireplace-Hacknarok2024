import random


class Room:
    def __init__(self, host_id, code) -> None:
        self.host = host_id
        self.code = code
        self.guests = []

    def add_guest(self, guest_id) -> None:
        self.guests.append(guest_id)

    def get_guest_ids(self):
        return self.guests


class RoomManager:
    def __init__(self) -> None:
        self.rooms = {"abcde": Room(1, "abcde")}

    def add_room(self) -> int:
        code = random.randint(0, 100000)
        self.rooms[code] = Room(None, code)
        return code

    def get_room(self, code: str) -> Room:
        return self.rooms[code]


room_manager = RoomManager()

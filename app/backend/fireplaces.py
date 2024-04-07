import uuid


class Fireplace:
    def __init__(self, host_id, code, title) -> None:
        self.host_id = host_id
        self.code = code
        self.title = title
        self.guests = []

    def add_guest(self, guest_id) -> None:
        self.guests.append(guest_id)

    def remove_guest(self, guest_id) -> None:
        self.guests.remove(guest_id)

    def get_guest_ids(self):
        return self.guests

    def __str__(self):
        return f"{self.host_id} {self.code} {self.title}"


class FireplaceManager:
    def __init__(self) -> None:
        self.fireplaces = {}

    def add_fireplace(self, host_id, title) -> int:
        code = str(uuid.uuid4())[:6]

        while not self.fireplaces.get(code, False):
            code = str(uuid.uuid4())[:6]
            self.fireplaces[code] = Fireplace(host_id, code, title)

        return code

    def get_fireplace(self, code: str) -> Fireplace:
        return self.fireplaces.get(code, False)

    def get_fireplaces(self) -> list[Fireplace]:
        return self.fireplaces.items()

    def remove_fireplace(self, code: str) -> None:
        if code in self.fireplaces:
            self.fireplaces.pop(code)


fireplace_manager = FireplaceManager()

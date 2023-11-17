from .event import Event


class Chapter:
    def __init__(self, id: int, events: Event, image: str):
        self.id = id
        self.events = events
        self.image = image

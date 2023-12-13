from models.story_element import StoryElement
from models.event import Event


class Chapter(StoryElement):
    def __init__(self, id: int, events: list[Event], image: str | None = None):
        super().__init__(image)
        self.id = id
        self.events = events

    def get_events(self) -> list[Event]:
        return self.events

from models.story_element import StoryElement
from models.event import Event


class Chapter(StoryElement):
    def __init__(self, id: int, events: list[Event], image: str | None = None):
        super().__init__(image)
        self.id = id
        self.events = events

    def get_events(self) -> list[Event]:
        return self.events
    
    def __eq__(self, __value: object) -> bool:
        print()
        return self.id == __value.id and len(self.events) == len(__value.events) and self.image == __value.image

    
    def __hash__(self) -> int:
        return hash((self.id, self.events))

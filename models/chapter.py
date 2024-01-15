from models.story_element import StoryElement
from models.event import Event
# The Chapter Type depends on the id and story time
class Chapter(StoryElement):
    def __init__(self, id: int, events: list[Event], image: str | None = None , chapterType: str | None = None):
        super().__init__(image)
        self.id = id
        self.events = events
        self.chapterType = chapterType

    def get_actions(self) -> list[Event]:
        events=[]
        for i in range(len(self.events)):
            if(self.events[i].dynamic == 'action'):
                events.append(self.events[i])
        return events
    
    def get_relationships(self) -> list[Event]:
        relationships=[]
        for i in range(len(self.events)):
            if(self.events[i].dynamic == 'relationship'):
                relationships.append(self.events[i])
        return relationships


    def get_type(self) -> str:
        return self.chapterType
    
    def __eq__(self, __value: object) -> bool:
        return self.id == __value.id and len(self.events) == len(__value.events) and self.image == __value.image

    
    def __hash__(self) -> int:
        return hash((self.id, self.events))

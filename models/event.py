from .character import Character
from .action import Action
class Event:
    def __init__(self, subjects: Character, objects: Character, action: Action):
        self.subjects = subjects
        self.objects = objects
        self.action = action


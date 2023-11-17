from models.dynamics.base_dynamic import BaseDynamic
from .character import Character
from .dynamics.action import Action
class Event:
    def __init__(self, subjects: Character, objects: Character, dynamic: BaseDynamic):
        self.subjects = subjects
        self.objects = objects
        self.dynamic = dynamic


from models.dynamics.base_dynamic import BaseDynamic
from .character import Character


class Event:
    def __init__(self, subjects: Character, objects: Character, dynamic: BaseDynamic):
        self.subjects = subjects
        self.objects = objects
        self.dynamic = dynamic

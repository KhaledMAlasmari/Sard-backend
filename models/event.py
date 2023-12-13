from models.dynamics.base_dynamic import BaseDynamic
from models.story_element import StoryElement
from .character import Character


class Event(StoryElement):
    def __init__(
        self,
        subjects: list[StoryElement],
        objects: list[StoryElement],
        dynamic: BaseDynamic,
        image: str | None = None,
    ):
        self.subjects = subjects
        self.objects = objects
        self.dynamic = dynamic
        super().__init__(image)

    def __str__(self) -> str:
        if self.image_description:
            place = f" in {self.image_description}"
        else:
            place = ""
        return f"{', '.join([str(subject) for subject in self.subjects])} {str(self.dynamic)} {', '.join([str(object) for object in self.objects])}{place}."

    def get_subjects(self) -> list[StoryElement]:
        return self.subjects

    def get_objects(self) -> list[StoryElement]:
        return self.objects

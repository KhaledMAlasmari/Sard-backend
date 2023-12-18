from models.dynamics.base_dynamic import BaseDynamic
from models.story_element import StoryElement


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

    def __eq__(self, __value: object) -> bool:
        return (
            isinstance(__value, Event)
            and self.subjects == __value.subjects
            and self.objects == __value.objects
            and self.dynamic == __value.dynamic
            and self.image_description == __value.image_description
        )

    
    def __hash__(self) -> int:
        return hash((self.__str__()))

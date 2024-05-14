from models.story_element import StoryElement


class Character(StoryElement):
    def __init__(self, name: str, image: str | None = None) -> None:
        self.name = name
        self.image = image
        super().__init__(image)

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def is_name_empty(self) -> bool:
        return self.name is None or self.name == ""

    def __str__(self) -> str:
        return self.name
    
    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and self.image == __value.image
    
    def __hash__(self) -> int:
        return hash((self.name, self.image))

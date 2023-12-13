from abc import ABC


class StoryElement(ABC):
    def __init__(self, image) -> None:
        self.image = image
        self.image_description = None

    def set_description_for_image(self, description) -> None:
        self.image_description = description
    
    def get_description_for_image(self) -> str:
        return self.image_description

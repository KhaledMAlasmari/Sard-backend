from abc import ABC


class StoryElement(ABC):
    def __init__(self, image) -> None:
        self.image = image
        self.image_description = None

    def set_description_for_image(self, description) -> None:
        self.image_description = description

    def get_description_for_image(self) -> str:
        return self.image_description
    
    
    def __eq__(self, __value: object) -> bool:
        return (
            isinstance(__value, StoryElement)
            and self.image == __value.image
            and self.image_description == __value.image_description
        )
        
    def __hash__(self) -> int:
        return hash((self.image, self.image_description))

import base64
import os
from ai.base_model import BaseModel
from openai import OpenAI

from services.openai import OpenAiAPI


class ImageToText(BaseModel):
    def __init__(self):
        self.model = OpenAiAPI()

    def get_description_for_character_image(self, image: str, name: str) -> str:
        #return self.model.get_description_for_character_image(image, name)
        pass
    def get_description_for_chapter_image(self, image: str) -> str:
        #return self.model.get_description_for_chapter_image(image)
        pass

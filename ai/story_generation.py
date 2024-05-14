import base64
import os
from ai.base_model import BaseModel
from openai import OpenAI

from services.openai import OpenAiAPI


class StoryGeneration(BaseModel):
    def __init__(self):
        self.model = OpenAiAPI()

    def generate_story(self, prompt: str) -> str:
        return self.model.generate_story_from_prompt(prompt)

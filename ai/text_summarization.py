import base64
import os
from ai.base_model import BaseModel
from openai import OpenAI

from services.openai import OpenAiAPI


class TextSummarization(BaseModel):
    def __init__(self):
        self.model = OpenAiAPI()

    def summerize_chapter(self, chapter_text: str) -> str:
        return self.model.get_summary_for_chapter(chapter_text)

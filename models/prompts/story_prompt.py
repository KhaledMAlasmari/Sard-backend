from models.event import Event
from models.prompts.base_prompt import BasePrompt

#TODO: FIGURE OUT WHETHER WE WANT A STORY PROMPT OR A CHAPTER PROMPT
class StoryPrompt(BasePrompt):
    def __init__(self):
        super().__init__(self.__get_prompt())

    def add_genre(self, genre: str):
        self.prompt = self.prompt.replace("[genre]", genre)

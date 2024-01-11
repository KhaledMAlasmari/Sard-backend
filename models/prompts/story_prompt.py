from models.prompts.base_prompt import BasePrompt
from models.story import Story


class StoryPrompt(BasePrompt):
    def __init__(self, story: Story):
        self.story = story
        self.genre = story.genre
        self.author_name = story.author_name
        # added story type
        self.story_type = story.story_type

    def get_prompt(self):
        if self.story_type is None:
            if self.author_name is None:
                return f"Persona: \"\"\"<you are a famous writer, you are writing a {self.genre} story, you will help the writers cause you are the best.>\"\"\""
            else:
                return f"Persona: \"\"\"<you are a famous writer, you are mimicking {self.author_name}, you are writing a {self.genre} story, you will help the writers cause you are the best.>\"\"\""
        else:
            if self.author_name is None:
                return f"Persona: \"\"\"<you are a famous writer, you are writing a {self.genre} story, you will help the writers cause you are the best.>\"\"\""
            else:
                return f"Persona: \"\"\"<you are a famous writer, you are mimicking {self.author_name}, you are writing a {self.genre} story and following the {self.story_type} rules, you will help the writers cause you are the best.>\"\"\""


    def __eq__(self, __value: object) -> bool:
        return self.genre == __value.genre and self.author_name == __value.author_name

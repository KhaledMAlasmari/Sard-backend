from models.prompts.base_prompt import BasePrompt


class StoryPrompt(BasePrompt):
    def __init__(self, genre, author_name: str|None = None):
        self.genre = genre
        self.author_name = author_name

    def get_prompt(self):
        if self.author_name is None:
            return f"you are a famous writer, you are writing a {self.genre} story, you will help the writers cause you are the best."
        else:
            return f"you are a famous writer, you are mimicking {self.author_name}, you are writing a {self.genre} story, you will help the writers cause you are the best."

from models.chapter import Chapter


class Story:
    def __init__(self, chapters: list[Chapter], genre: str) -> None:
        self.chapters = chapters
        self.genre = genre

    def generate(self) -> None:
        pass

    def add_prompt(self, prompt: str) -> None:
        self.prompt = prompt

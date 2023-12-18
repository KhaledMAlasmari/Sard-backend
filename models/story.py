from models.chapter import Chapter


class Story:
    def __init__(self, chapters: list[Chapter], genre: str, authoe_name: str | None) -> None:
        self.chapters = chapters
        self.genre = genre
        self.authoe_name = authoe_name

    def generate(self) -> None:
        pass
        
    def __eq__(self, __value: object) -> bool:
        return self.chapters == __value.chapters and self.genre == __value.genre

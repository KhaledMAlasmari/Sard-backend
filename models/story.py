from models.chapter import Chapter
from models.ChapterGraph import Graph


class Story:
    def __init__(self, chapters: list[Chapter], genre: str, author_name: str | None=None) -> None:
        self.chapters = chapters
        self.genre = genre
        self.author_name = author_name

    def generate(self) -> None:
        pass
    
    def get_graph(self, graphs: list[Graph]):
        self.graphs = graphs
        return self.graphs
    
    def __eq__(self, __value: object) -> bool:
        return self.chapters == __value.chapters and self.genre == __value.genre

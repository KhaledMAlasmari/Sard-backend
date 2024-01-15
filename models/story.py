from models.chapter import Chapter
from models.ChapterGraph import Graph
from utils.extract_data import extract_graphs

class Story:
    def __init__(self, chapters: list[Chapter], genre: str, author_name: str | None=None, story_type: str | None= None) -> None:
        self.chapters = chapters
        self.genre = genre
        self.author_name = author_name
        self.story_type = story_type
        self.graphs = extract_graphs(chapters)
    def generate(self) -> None:
        pass
    
    def get_graph(self):
        return self.graphs
    
    def __eq__(self, __value: object) -> bool:
        return self.chapters == __value.chapters and self.genre == __value.genre

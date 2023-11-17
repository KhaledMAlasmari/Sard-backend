from models.story import Story
from utils.extract_data import extract_chapters

def generate_story(data: dict):
    genre = data['genre']
    chapters = extract_chapters(data)
    story = Story(genre=genre, chapters=chapters)
    story.add_prompt()
    

from models.prompts.story_prompt import StoryPrompt
from models.story import Story
from utils.extract_data import extract_chapters


def generate_story(data: dict):
    genre = data["genre"]
    author_name = data["author_name"]
    chapters = extract_chapters(data)
    story = Story(genre=genre, chapters=chapters, authoe_name=author_name)
    #TODO: CONTINUE THIS TO GENERATE STORY
    #story_prompt = StoryPrompt(story)
    
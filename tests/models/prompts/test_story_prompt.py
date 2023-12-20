import unittest

from models.prompts.story_prompt import StoryPrompt
from models.story import Story


class TestEventPrompt(unittest.TestCase):
    def test_get_prompt_with_author(self):
        author_name = "Stephen King"
        genre = "horror"
        story = Story([], genre, author_name)
        story_prompt = StoryPrompt(story)
        expected_prompt = f"Persona: \"\"\"<you are a famous writer, you are mimicking {author_name}, you are writing a {genre} story, you will help the writers cause you are the best.>\"\"\""
        self.assertMultiLineEqual(story_prompt.get_prompt(), expected_prompt)

    def test_get_prompt_without_author(self):
        genre = "horror"
        story = Story([], genre)
        story_prompt = StoryPrompt(story)
        expected_prompt = f"Persona: \"\"\"<you are a famous writer, you are writing a {genre} story, you will help the writers cause you are the best.>\"\"\""
        self.assertMultiLineEqual(story_prompt.get_prompt(), expected_prompt)


if __name__ == "__main__":
    unittest.main()

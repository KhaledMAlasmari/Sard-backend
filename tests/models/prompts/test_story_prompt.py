import unittest

from models.prompts.story_prompt import StoryPrompt


class TestEventPrompt(unittest.TestCase):
    def test_get_prompt_with_author(self):
        author_name = "Stephen King"
        genre = "horror"
        story = StoryPrompt(genre, author_name)
        expected_prompt = f"you are a famous writer, you are mimicking {author_name}, you are writing a {genre} story, you will help the writers cause you are the best."
        self.assertMultiLineEqual(story.get_prompt(), expected_prompt)

    def test_get_prompt_without_author(self):
        genre = "horror"
        story = StoryPrompt(genre)
        expected_prompt = f"you are a famous writer, you are writing a {genre} story, you will help the writers cause you are the best."
        self.assertMultiLineEqual(story.get_prompt(), expected_prompt)


if __name__ == "__main__":
    unittest.main()

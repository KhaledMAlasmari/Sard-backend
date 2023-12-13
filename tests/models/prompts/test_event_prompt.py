import unittest

from models.dynamics.action import Action
from models.character import Character
from models.event import Event
from models.prompts.event_prompt import EventPrompt


class TestEventPrompt(unittest.TestCase):
    def test_get_prompt_one_subject_one_object(self):
        subjects = [Character("Khaled")]
        objects = [Character("Ahmed")]
        action = Action("talked with")
        event = Event(subjects, objects, action)
        event_prompt = EventPrompt(event)
        expected_prompt = "Khaled talked with Ahmed."
        self.assertEqual(event_prompt.get_prompt(), expected_prompt)

    def test_get_prompt_multiple_subjects_one_object(self):
        subjects = [Character("Khaled"), Character("Omar")]
        objects = [Character("Ahmed")]
        action = Action("fought")
        event = Event(subjects, objects, action)
        event_prompt = EventPrompt(event)
        expected_prompt = "Khaled, Omar fought Ahmed."
        self.assertEqual(event_prompt.get_prompt(), expected_prompt)

    def test_get_prompt_one_subject_multiple_object(self):
        subjects = [Character("Ahmed"), Character("Omar")]
        objects = [Character("Khaled")]
        action = Action("walked to")
        event = Event(subjects, objects, action)
        event_prompt = EventPrompt(event)
        expected_prompt = "Ahmed, Omar walked to Khaled."
        self.assertEqual(event_prompt.get_prompt(), expected_prompt)

    def test_get_prompt_multiple_subjects_multiple_object(self):
        subjects = [Character("Ahmed"), Character("Omar")]
        objects = [Character("Khaled"), Character("Ali")]
        action = Action("played with")
        event = Event(subjects, objects, action)
        event_prompt = EventPrompt(event)
        expected_prompt = "Ahmed, Omar played with Khaled, Ali."
        self.assertEqual(event_prompt.get_prompt(), expected_prompt)


if __name__ == "__main__":
    unittest.main()

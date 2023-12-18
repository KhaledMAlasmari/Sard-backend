import unittest
from models.chapter import Chapter
from models.event import Event
from models.dynamics.action import Action
from models.character import Character
from utils.extract_data import extract_chapters

class TestExtractData(unittest.TestCase):
    def test_extract_chapters(self):
        data = {
            "genere": "Adventure",
            "chapters": [
                {
                    "id": 1,
                    "events": [
                        {
                            "subjects": [
                                {
                                    "name": "John",
                                    "image": "john.png",
                                    "type": "character"
                                }
                            ],
                            "objects": [
                                {
                                    "name": "Apple",
                                    "image": "apple.png",
                                    "type": "character"
                                }
                            ],
                            "dynamic": {
                                "type": "action",
                                "name": "Eating"
                            }
                        }
                    ],
                    "image": "chapter1.png"
                }
            ]
        }
        # Call function with validated data
        result = extract_chapters(data)

        # Assert that the result matches the expected output
        # The expected output depends on the implementation of `extract_chapters`
        # Replace `expected_output` with the expected result
        expected_output = [
            Chapter(
                id=1,
                events=[
                    Event(
                        subjects=[Character(name="John", image="john.png")],
                        objects=[Character(name="Apple", image="apple.png")],
                        dynamic=Action(description="Eating"),
                    )
                ],
                image="chapter1.png",
            )
        ]
        self.assertCountEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

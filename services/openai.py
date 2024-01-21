import os
from openai import OpenAI


class OpenAiAPI:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def get_description_for_character_image(self, image: str, name: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"describe the character appearance in detail for the attached image. The character name is {name}, refrain from using he, she it, please use the character name instead. Make sure you start describing the character immeditly do not use words like 'Certainly', 'Okay'. If you do not recieve an image, respond with nothing. As in empty text!!!",
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": image},
                            "detail": "Low"

                        },
                    ],
                }
            ],
            # subject to change
            max_tokens=2000,
        )
        return response.choices[0].message.content or ""

    def get_description_for_chapter_image(self, image: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        [
                            {
                                "type": "text",
                                "text": "This image represent a place where events happened. Describe the place in detail. If the image has characters in it, do not describe them and ignore them. Your main focus is to describe the place and it's surroundings in detail.",
                            },
                            {
                                "type": "image_url",
                                "image_url": {"url": image},
                                "detail": "Low"
                            },
                        ]
                    ],
                }
            ],
            # subject to change
            max_tokens=2000,
        )
        return response.choices[0].message.content or ""

    def get_summary_for_chapter(self, chapter: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize the following chapter in a short and concise way. Make sure you include all the important events in your summary as next chapters will depend on it:\n{chapter}",
                }
            ],
            # subject to change
            max_tokens=2000,
        )
        return response.choices[0].message.content or ""

    def generate_story_from_prompt(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[{"role": "user", "content": prompt}],
            # subject to change
            max_tokens=2000,
        )
        return response.choices[0].message.content or ""

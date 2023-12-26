from models.chapter import Chapter
from models.event import Event
from models.character import Character
from models.prompts.base_prompt import BasePrompt


class ChapterPrompt(BasePrompt):
    def __init__(self, chapter: Chapter, previous_chapters_summary: str | None = None):
        self.chapter = chapter
        self.events: list[Event] = self.chapter.get_events()
        self.chapterType: str = self.chapter.get_type()
        self.previous_chapters_summary = previous_chapters_summary

    def get_prompt(self) -> str:
        place = self._get_place()
        characters = self._get_characters()
        previous_chapters_summary = self.get_summary()
        # f strings cannot contain backslashes, so we use the following:
        new_line = "\n"
        # added one to the chapter id because the chapter id starts from 0
        return f"""Request: \"\"\"<Write chapter {self.chapter.id + 1} with dialogues using the following characters details:
{new_line.join([f'[character name: {character.name}{new_line}character details: {character.get_description_for_image()}]' for character in characters])}
now map it to the the information you have in the following events:
{new_line.join([f'[{event}]' for event in self.chapter.events])}
{previous_chapters_summary}
{place}>\"\"\"
Output Length: \"\"\"<3000 words>\"\"\"
Structure: \"\"\"<You are writing a {self.chapterType} chapter, follow the rules to write an amazing {self.chapterType}> \"\"\"
Take your time with the writing, perfection this chapter and make it as a one piece without divisions.""".strip()
    
    

    def get_summary(self) -> str:
        if self.previous_chapters_summary:
            return f"Use previous chapter information: \"\"\"<Summary:\n{self.previous_chapters_summary}>\"\"\""
        else:
            return ""

    def set_summary(self) -> str:
        if self.previous_chapters_summary:
            return f"Use previous chapter information: \"\"\"<Summary:\n{self.previous_chapters_summary}>\"\"\""
        else:
            return ""
    def _get_place(self) -> str:
        if self.chapter.get_description_for_image():
            return (
                f"those events happened in {self.chapter.get_description_for_image()}."
            )
        else:
            return ""

    def _get_characters(self) -> list[Character]:
        subjects = [
            character
            for event in self.chapter.events
            for character in event.get_subjects()
            if isinstance(character, Character)
        ]
        objects = [
            character
            for event in self.chapter.events
            for character in event.get_objects()
            if isinstance(character, Character)
        ]
        characters = subjects + objects
        characters = list(set(characters))
        characters = sorted(characters, key=lambda character: character.name)
        return characters


    def __eq__(self, __value: object) -> bool:
        return self.chapter == __value.chapter and self.previous_chapters_summary == __value.previous_chapters_summary

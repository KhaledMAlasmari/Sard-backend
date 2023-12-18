from models.event import Event
from models.prompts.base_prompt import BasePrompt


class EventPrompt(BasePrompt):
    def __init__(self, event: Event):
        self.event = event
        self.prompt = self.get_prompt()

    def get_prompt(self) -> str:
        return f"""{str(self.event)}"""

    def __eq__(self, __value: object) -> bool:
        return self.event == __value.event

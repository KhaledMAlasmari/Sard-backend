from abc import ABC, abstractmethod


class BasePrompt(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_prompt(self):
        pass

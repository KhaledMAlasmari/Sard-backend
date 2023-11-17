from models.dynamics.base_dynamic import BaseDynamic


class Action(BaseDynamic):
    def __init__(self, name):
        self._name = name
        self.type = "action"
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

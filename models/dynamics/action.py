from models.dynamics.base_dynamic import BaseDynamic


class Action(BaseDynamic):
    def __init__(self, description):
        super().__init__("action", description)

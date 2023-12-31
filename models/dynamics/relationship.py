from models.dynamics.base_dynamic import BaseDynamic


class Relationship(BaseDynamic):
    def __init__(self, description):
        super().__init__("relationship", description)

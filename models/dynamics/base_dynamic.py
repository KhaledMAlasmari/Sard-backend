class BaseDynamic:
    def __init__(self, type: str, description: str) -> None:
        self.type = type
        self.description = description
    
    def __str__(self) -> str:
        return self.description

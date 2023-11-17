class Character:
    def __init__(self, name: str, image: str) -> None:
        self.__name = name
        self.__image = image

    def get_image(self) -> str:
        return self.__image

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def is_name_empty(self) -> bool:
        return self.__name is None or self.__name == ""

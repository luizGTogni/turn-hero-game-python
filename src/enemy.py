from character import Character

class Enemy(Character):
    def __init__(self, name: str, life: int, level: int, type: str):
        super().__init__(name, life, level)
        self.__type = type

    @property
    def type(self):
        return self.__type

from character import Character

class Player(Character):
    def __init__(self, name: str, life: int, level: int, skill: str):
        super().__init__(name, life, level)
        self.__skill = skill

    @property
    def skill(self):
        return self.__skill

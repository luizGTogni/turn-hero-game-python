from random import randint

class Character:
    def __init__(self, name: str, life: int, level: int):
        self.__name = name
        self.__life = life
        self.__level = level
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def life(self) -> int:
        return self.__life
    
    @property
    def level(self) -> int:
        return self.__level

    def to_receive_damage(self, value: int) -> None:
        self.__life -= value
        if self.life < 0:
            self.__life = 0

    def attack(self, target: 'Character') -> None:
        if self.life > 0:
            damage = randint(self.level * 2, self.level * 4)
            target.to_receive_damage(damage)
            print(f'{self.name} attacks {target.name} and deals {damage} damage.')

    def __str__(self) -> str:
        text = ''
        for k, v in self.__dict__.items():
            text += f'\n{k.split('__')[1].capitalize()}: {v}'
        return text
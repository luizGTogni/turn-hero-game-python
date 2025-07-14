import os

from player import Player
from enemy import Enemy

class Game:
    def __init__(self) -> None:
        self.player = Player(name='Hero', life=100, level=3, skill='Super Strength')
        self.enemy = Enemy(name='Bat', life=50, level=5, type='Normal')
        self.__round = 1
    
    def next_round(self) -> None:
        self.__round += 1

    def start(self) -> None:
        print('Game Started!')

        while self.player.life > 0 and self.enemy.life > 0:
            print(f'Round {self.__round}')

            print(self.player)
            print(self.enemy)

            input('\nPress Enter to attack...')
            op = int(input('Choose (1 - Attack, 2 - Special Attack): '))

            if op == 1:
                self.player.attack(target=self.enemy)
                self.enemy.attack(target=self.player)
                self.next_round()
            elif op == 2:
                self.next_round()
            else:
                print('Invalid Option!')

            input('\nGo to next round...')
            os.system('cls' if os.name == 'nt' else 'clear')
        
        if self.player.life > 0:
            print(f'{self.player.name} Winner!')
            return
        
        print(f'{self.enemy.name} Winner')

game = Game()
game.start()
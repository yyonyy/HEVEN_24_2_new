import random

class Dicegame():
    def __init__(self,N):
        self.N = N
        self.dice_num = [0,0,0,0,0,0,0]

    def roll_dice(self):
        for i in range(self.N):
            self.dice_num[random.randint(1,6)]+=1

    def print_result(self):
        for i in range(1,7):
            print(f'Dice number {i} : {self.dice_num[i]}')
        self.dice_num[self.dice_num.index(max(self.dice_num))] = 0
        second_max = max(self.dice_num)
        for i in range(1,7):
            if self.dice_num[i] == second_max:
                print(f'Second Largest Number : {i}')
        
N = int(input())
dice = Dicegame(N)
dice.roll_dice()
dice.print_result()

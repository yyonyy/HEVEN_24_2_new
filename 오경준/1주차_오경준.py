import random

class Dicegame():
    def __init__(self,N):
        self.N = N
        self.dice_num = []

    def roll_dice(self):
        for _ in range(int(self.N)):
            self.dice_num.append(random.randint(1,6))

    def print_result(self):
        num = 1
        for i in self.dice_num:
            print(f'Dice number {num} : {i}')
            num += 1

        num1 = 1
        list1 = []
        for j in range(6):
            list1.append(self.dice_num.count(num1))
            num1 +=1
        first = max(list1)
        second = 0
        for num in list1:
            if num != first:
                second = max(second,num)


        second_list = [i + 1 for i, count in enumerate(list1) if count == second]
        print(f'Second Largest NUmber : {second_list}')

            
N = input()
dice = Dicegame(N)
dice.roll_dice()
dice.print_result()

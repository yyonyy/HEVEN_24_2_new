import random
from collections import Counter

class DiceGame:
    def __init__(self,N):
        self.N = N
        self.dice_num = [0,0,0,0,0,0]
        self.rolls = []
    
    #입력받은 횟수만큼 주사위 던지고, 나온 모든 결과를 리스트에 저장
    def roll_dice(self):
        for _ in range(self.N):
            ran = random.randint(1,6)
            self.rolls.append(ran)
            self.dice_num[ran-1] += 1

    #주사위 던진 결과 모두 출력, 두 번째로 많이 나온 주사위 눈 출력
    def print_result(self):
        for i in range(1,7):
            print(f"Dice number {i} : {self.dice_num[i-1]}")

        count = Counter(self.rolls)

        most_common = count.most_common()
        if len(most_common) < 2:
            print("Not found")
        else:
            print(f"Second Largest Number : {most_common[1][0]}")

N = int(input())
if N>10 and N<50:
    dice = DiceGame(N)
    dice.roll_dice()
    dice.print_result()
else:
    print("Try again")
    

import random

class Dicegame:
    def __init__(self, N):
        self.N = N
        self.dice_num = [0] * 6
            
    def roll_dice(self):
        for _ in range(self.N):
            roll = random.randint(1,6)
            self.dice_num[roll - 1] += 1

    def print_result(self):
        for i in range(6):
            print(f"Dice number {i + 1} : {self.dice_num[i]}")

        sorted_counts = sorted(set(self.dice_num), reverse = True)

        if len(sorted_counts) > 1:
            second_largest = sorted_counts[1]
            for i in range(6):
                if self.dice_num[i] == second_largest:
                    print(f"Second Largest Number : {i + 1}")

#주사위 던질 횟수 입력받기
while True:
    N = int(input("주사위 던질 횟수(10~50): "))
    if 10 <= N <= 50:
        break
    else:
        print("잘못된 입력입니다.")

#Dicegame 클래스 생성 및 실행
game = Dicegame(N)
game.roll_dice()
game.print_result()
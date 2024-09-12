import random
from collections import Counter

class Dicegame:
    def __init__(self):
        while True:
            self.N = int(input("주사위를 던질 횟수를 입력하세요 (11-49): "))
            if 10 < self.N < 50:
                break
            print("11에서 49 사이의 숫자를 입력해주세요.")
        
        self.dice_num = [0] * 6
        self.results = []

    def roll_dice(self):
        for _ in range(self.N):
            roll = random.randint(1, 6)
            self.results.append(roll)
            self.dice_num[roll - 1] += 1

    def print_result(self):
        print(f"{self.N}")
        for i, count in enumerate(self.dice_num, 1):
            print(f"Dice number {i} : {count}")
        
        counts = Counter(self.results)
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))
        
        if len(sorted_counts) > 1:
            second_highest_count = sorted_counts[1][1]
            second_highest_numbers = [num for num, count in sorted_counts if count == second_highest_count]
            
            for num in second_highest_numbers:
                print(f"Second Largest Number : {num}")
        else:
            print("Second Largest Number : None")

# 사용 예시
game = Dicegame()
game.roll_dice()
game.print_result()
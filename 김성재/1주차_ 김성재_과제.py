import random
from collections import Counter

class DiceGame:
    def __init__(self, num_rolls):
        if not 10 < num_rolls < 50:
            raise ValueError("주사위 던지는 횟수는 10과 50 사이여야 합니다.")
        self.N = num_rolls
        self.dice_num = [0] * 6
        self.results = []

    def roll_dice(self):
        for _ in range(self.N):
            dice_roll = random.randint(1, 6)
            self.results.append(dice_roll)
            self.dice_num[dice_roll - 1] += 1

    def print_result(self):
        counts = Counter(self.results)

        # 1부터 6까지 순서대로 눈금별 횟수 출력
        for num in range(1, 7):
            count = counts.get(num, 0)
            print(f"Dice number {num} : {count}")
        # 가장 빈번한 숫자들의 횟수 구하기
        most_common_counts = [count for num, count in counts.most_common()]
        most_common_count = most_common_counts[0]

        # 두 번째로 빈번한 횟수 구하기
        second_most_common_count = max(count for count in counts.values() if count < most_common_count)

        # 두 번째로 빈번한 숫자 찾기
        second_most_common_numbers = [num for num, count in counts.items() if count == second_most_common_count]

        for number in second_most_common_numbers:
            print("Second Largest Number : ", number)

N = int(input())
game = DiceGame(N)
game.roll_dice()
game.print_result()
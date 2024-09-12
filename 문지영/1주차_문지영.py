import random

class Dicegame:
    def __init__(self):
        self.dice = []
        self.dice_num = []

    def roll_dice(self):
        while True:
                self.N = int(input())
                if 10 < self.N < 50:
                    break
                else:
                    print("10과 50 사이의 수를 입력해주십시오.")

    def print_result(self):
        for i in range(1, 7):
            num_count = self.dice.count(i)
            print(f"Dice number {i} : {num_count}")
            self.dice_num.append(num_count)

        sorted_counts = sorted(self.dice_num, reverse=True)
        first_max_value = sorted_counts[0]
        for value in sorted_counts:
            if value < first_max_value:
                second_max_value = value
                break
        else:
            print("두 번째로 큰 값이 존재하지 않습니다.")

        second_max_indexes = [i + 1 for i, count in enumerate(self.dice_num) if count == second_max_value]
        for index in second_max_indexes:
            print(f"Second Largest Number : {index}")

game = Dicegame()
game.roll_dice()
game.print_result()

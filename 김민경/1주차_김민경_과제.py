import random
from collections import Counter

class dicegame:
    def __init__(self, n):
        if n <= 10 or n >= 50:
            raise ValueError("주사위를 던질 횟수는 10보다 크고 50보다 작아야 합니다.")
        self.N = n
        self.dice_num = [0] * 6  
    def roll_dice(self):
        results = [random.randint(1, 6) for _ in range(self.N)]
        for result in results:
            self.dice_num[result - 1] += 1  

    def print_result(self):
        # 주사위 눈별 빈도 출력
        for i in range(6):
            print(f"Dice number {i + 1} : {self.dice_num[i]}")
        
        counts = Counter(self.dice_num)
        most_common = counts.most_common()
        
        if len(most_common) < 2:
            print("두 번째로 많이 나온 눈을 찾을 수 없습니다.")
            return

        frequency_counts = sorted(set(self.dice_num), reverse=True)
        
        if len(frequency_counts) < 2:
            print("두 번째로 많이 나온 눈이 없습니다.")
            return

        highest_count = frequency_counts[0]
        second_highest_count = frequency_counts[1]

        second_most_common_numbers = [i + 1 for i, count in enumerate(self.dice_num) if count == second_highest_count]
        
        if second_most_common_numbers:
            print("Secong Largest Number : ", end='')
            print(' '.join(map(str, second_most_common_numbers)))
        else:
            print("두 번째로 많이 나온 주사위 눈이 없습니다.")

if __name__ == "__main__":
    n = int(input())
    try:
        game = dicegame(n)
        game.roll_dice()
        game.print_result()
    except ValueError as e:
        print(e)

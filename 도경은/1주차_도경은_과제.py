import random
from collections import Counter

class Dicegame:
    def __init__(self, n):
        self.n = n
        self.results = []

    def roll_dice(self):
        self.results = [random.randint(1, 6) for _ in range(self.n)]

    def print_result(self):
        for i in range(len(self.results)):
            print("Dice number ", i, ": ", self.results[i])
        

        count = Counter(self.results)
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        second_most_freq = sorted_count[1][1]
        
        
        second_most_numbers = [number for number, freq in sorted_count if freq == second_most_freq]
        
        for i in range(len(sorted(second_most_numbers))):
            print("Second Largest Number : ", sorted(second_most_numbers)[i])

# 사용 예제
if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            game = Dicegame(n)
            game.roll_dice()
            game.print_result()
            break
        except ValueError as e:
            print(e)

import random

class Dicegame:
    def __init__(self, N):
        self.N = N
        self.rolls = []

    def roll_dice(self):
        for _ in range(self.N):
            roll = random.randint(1, 6)
            self.rolls.append(roll)

    def print_result(self):

        for i, roll in enumerate(self.rolls, 1):
            print(f"Dice number {i}: {roll}")

        counts = [self.rolls.count(i) for i in range(1, 7)]
        
        sorted_counts = sorted(set(counts), reverse=True)
        
        if len(sorted_counts) < 2:
            print("No second largest value.")
            return
        
        second_largest_count = sorted_counts[1]
        
        second_largest_numbers = [i+1 for i, count in enumerate(counts) if count == second_largest_count]
        
        if second_largest_numbers:
            for num in second_largest_numbers:
                print(f"Second Largest Number : {num}")
        else:
            print("No second largest number found.")

if __name__ == "__main__":
    N = int(input())
    if N >10 and N <50 :
        game = Dicegame(N)
        game.roll_dice()
        game.print_result()

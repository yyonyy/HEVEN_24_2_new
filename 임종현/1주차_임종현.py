import random
from collections import Counter

class Dicegame:
    def __init__(self, N):
        111
        if 10 < N < 50:
            self.N = N
        else:
            raise ValueError("N must be between 10 and 50.")
        self.dice_num = [0] * 6  
    
    def roll_dice(self):
        
        self.results = []
        for _ in range(self.N):
            roll = random.randint(1, 6)
            self.results.append(roll)
            self.dice_num[roll - 1] += 1
    
    def print_result(self):
        
        for i in range(6):
            print(f"Dice number {i+1} : {self.dice_num[i]}")
        
        
        counts = Counter(self.results)
        sorted_counts = counts.most_common()
        max_count = sorted_counts[0][1]
        
        
        second_largest_count = [item for item in sorted_counts if item[1] < max_count]
        
        if second_largest_count:
            second_max = second_largest_count[0][1]
            second_largest_numbers = [item[0] for item in second_largest_count if item[1] == second_max]
            
            for num in second_largest_numbers:
                print(f"Second Largest Number : {num}")
        else:
            print("No second largest number")


N = int(input())


dice_game = Dicegame(N)
dice_game.roll_dice()
dice_game.print_result()

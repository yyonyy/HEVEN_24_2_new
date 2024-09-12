import random
from collections import Counter

class Dicegame:
    def __init__(self):
        while True:
            try:
                self.N = int(input())
                if 10 < self.N < 50:
                    break
                else:
                    print("10과 50 사이의 정수를 입력하시오")
            except ValueError:
                print("타당한 정수 값을 입력하시오")
        
        self.dice_results = []
    
    def roll_dice(self):
        for _ in range(self.N):
            self.dice_results.append(random.randint(1, 6))
    
    def print_result(self):
        dice_counts = Counter(self.dice_results)
        
        for i in range(1, 7):
            print(f"Dice number {i} : {dice_counts[i]}")
        
        most_common = dice_counts.most_common()  
      
        if len(most_common) > 1:
            first_max = most_common[0][1]  
            second_max = None
            for count in most_common:
                if count[1] < first_max:
                    if second_max is None:
                        second_max = count[1]
                    if count[1] == second_max:
                        print(f"Second Largest Number : {count[0]}")
        else:
            print("There is no second largest number.")


game = Dicegame()
game.roll_dice()
game.print_result()


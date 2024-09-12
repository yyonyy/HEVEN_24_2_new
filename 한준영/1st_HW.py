import random
from collections import Counter

class Dicegame:
    def __init__(self, N):
   
        if 10 < N < 50:
            self.N = N
        else:
            raise ValueError("N must be between 10 and 50.")
        
     
        self.results = []

    def roll_dice(self):
        
        for _ in range(self.N):
            roll = random.randint(1, 6)  
            self.results.append(roll)
    
    def print_result(self):

        result_counts = Counter(self.results)

        for i in range(1, 7):
            print(f"Dice number {i} : {result_counts.get(i, 0)}")

        most_common = result_counts.most_common()

        if len(most_common) < 2:
            print("Not enough variety in the results.")
            return


        counts = sorted(set(result_counts.values()), reverse=True)
        
        if len(counts) > 1:
            second_max_count = counts[1]
        else:
            print("There is no second most frequent number.")
            return

     
        second_most_common = [face for face, count in result_counts.items() if count == second_max_count]


        for num in second_most_common:
            print(f"Second Largest Number : {num}")


if __name__ == "__main__":
        try:
                    
            N = int(input("Enter the number of dice rolls: "))
            game = Dicegame(N)
            

            game.roll_dice()
            game.print_result()
        
        except ValueError as e:
            print(e)
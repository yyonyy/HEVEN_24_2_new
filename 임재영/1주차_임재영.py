import random
from collections import Counter

class DiceGame:
    def __init__(self, N):
        self.N = N
        self.결과값 = []

    def roll_dice(self):
        주사위면 = [1, 2, 3, 4, 5, 6]
        self.결과값 = [random.choice(주사위면) for _ in range(self.N)]

    def get_result(self):
        return self.결과값

    def print_result(self):
        결과값수 = Counter(self.결과값)   
        
        for number in range(1, 7):
            print(f"Dice number {number} : {결과값수.get(number, 0)}")

        most_common = 결과값수.most_common()
        n_1f = most_common[0][1] 
        n_2f = None
        두번째높은수들 = []
        
        for number, 빈도 in most_common:
            if 빈도 < n_1f:
                if n_2f is None:
                    n_2f = 빈도
                if 빈도 == n_2f:
                    두번째높은수들.append(number)
        
        
        print("Second Largest Number :", ', '.join(map(str, sorted(두번째높은수들))))

if __name__ == "__main__":
    while True:
        try:
            N = int(input(""))
            if 10 <= N <= 50:
                break
        
        except ValueError:
            print("")

    game = DiceGame(N)
    game.roll_dice()
    game.print_result()

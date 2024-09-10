import random

class Dicegame:
    def __init__(self):
        self.seq_rolldice = []
        self.dice_num = []
    
    def roll_dice(self):
        while True:
            N = int(input("주사위를 몇 번 던지겠습니까?: "))
            if 10 < N < 50:
                for _ in range(N):
                    dicenum = random.randint(1, 6)
                    self.seq_rolldice.append(dicenum)
                break
            else:
                print("10 초과 50 미만의 횟수를 지정해 주십시오.")
    
    def print_results(self):
        for r in range(1, 7):
            number = self.seq_rolldice.count(r)
            print(f"Dice number {r}: {number}")
            self.dice_num.append(number)

        sorted_results = sorted(set(self.dice_num), reverse=True)
        if len(sorted_results) > 1:
            second_largest = sorted_results[1]
            for i in range(1, 7):
                if self.seq_rolldice.count(i) == second_largest:
                    print(f"Second Largest Number: {i}")

        else :
            print("주사위의 숫자가 모두 동일합니다.")

if __name__ == "__main__":
    dice1 = Dicegame()
    dice1.roll_dice()
    dice1.print_results()
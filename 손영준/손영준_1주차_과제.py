import random
from collections import Counter

class Dicegame:
    def __init__(self, N):
        if not (10 < N < 50):
            raise ValueError("N should be between 10 and 50")
        self.N = N
        self.results = []  # 주사위 던진 결과를 저장할 리스트

    def roll_dice(self):
        self.results = [random.randint(1, 6) for _ in range(self.N)]

    def print_result(self):
        # 주사위 던진 결과를 출력
        print("Dice Results:")
       
        # 각 눈의 출현 횟수 세기
        counts = Counter(self.results)
       
        # 1부터 6까지의 눈이 각각 몇 번 나왔는지 출력
        for i in range(1, 7):
            print(f"Dice number {i} : {counts.get(i, 0)}")

        # 출현 횟수를 기준으로 정렬
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        if len(sorted_counts) < 2:
            print("There are not enough unique dice results to find the second most common one.")
            return

        # 가장 많이 나온 주사위 눈의 출현 횟수
        most_common_count = sorted_counts[0][1]
       
        # 두 번째로 많이 나온 주사위 눈의 출현 횟수 찾기
        second_most_common_count = sorted_counts[1][1]

        # 두 번째로 많이 나온 주사위 눈들을 찾기
        second_most_common_numbers = [num for num, count in sorted_counts if count == second_most_common_count]

        # 두 번째로 많이 나온 숫자를 오름차순으로 정렬
        second_most_common_numbers.sort()

        # 각 두 번째로 많이 나온 숫자를 개별적으로 출력
        for num in second_most_common_numbers:
            print(f"Second Largest Number : {num}")

def main():
    # 사용자로부터 주사위 던질 횟수를 입력받음
    N = int(input("Enter the number of dice rolls (between 10 and 50): "))
   
    # 유효성 검사
    if not (10 < N < 50):
        print("The number of dice rolls must be between 10 and 50.")
        return

    # Dicegame 객체 생성 및 사용
    game = Dicegame(N)
    game.roll_dice()  # 주사위 던지기
    game.print_result()  # 결과 출력

if __name__ == "__main__":
    main()


import random
from collections import Counter

class dicegame:
    def __init__(self, n):
        if n <= 10 or n >= 50:
            raise ValueError("주사위를 던질 횟수는 10보다 크고 50보다 작아야 합니다.")
        self.N = n
        self.dice_num = [0] * 6  # 주사위 눈별로 나온 횟수를 저장하는 리스트

    def roll_dice(self):
        results = [random.randint(1, 6) for _ in range(self.N)]
        for result in results:
            self.dice_num[result - 1] += 1  # 눈의 개수에 따라 카운트 증가

    def print_result(self):
        # 주사위 결과와 빈도 출력
        print("주사위 눈별 빈도: ")
        for i in range(6):
            print(f"{i + 1}: {self.dice_num[i]}회")
        
        # 주사위 눈 빈도의 두 번째로 많은 값을 찾기
        counts = Counter(self.dice_num)
        most_common = counts.most_common()
        
        if len(most_common) < 2:
            print("두 번째로 많이 나온 눈을 찾을 수 없습니다.")
            return

        # 가장 많이 나온 빈도와 두 번째로 많이 나온 빈도를 구합니다
        highest_count = most_common[0][1]
        second_highest_count = None
        
        for num, count in most_common:
            if count < highest_count:
                second_highest_count = count
                break
        
        if second_highest_count is None:
            print("두 번째로 많이 나온 눈이 없습니다.")
            return

        # 두 번째로 많이 나온 빈도의 주사위 눈들을 찾기
        second_most_common_numbers = [i + 1 for i, count in enumerate(self.dice_num) if count == second_highest_count]
        
        if second_most_common_numbers:
            print("두 번째로 많이 나온 주사위 눈: ", end='')
            print(' '.join(map(str, second_most_common_numbers)))
        else:
            print("두 번째로 많이 나온 주사위 눈이 없습니다.")

# 사용 예시
if __name__ == "__main__":
    n = int(input("주사위를 던질 횟수를 입력하세요 (10 < n < 50): "))
    try:
        game = dicegame(n)
        game.roll_dice()
        game.print_result()
    except ValueError as e:
        print(e)

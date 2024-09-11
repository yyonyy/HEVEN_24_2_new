import random
from collections import Counter

class Dicegame:
    def __init__(self):
        self.results = []

    def roll_dice(self, N):
        
        self.results = [random.randint(1, 6) for _ in range(N)]

    def print_result(self):
        print("주사위 결과:", self.results)
        
        
        counter = Counter(self.results)
        
        most_common = counter.most_common()

        if len(most_common) > 1:
            second_most_common_count = most_common[1][1]
            second_most_common = [num for num, count in most_common if count == second_most_common_count]
            print("두 번째로 많이 나온 주사위 눈:", second_most_common)
        else:
            print("모든 주사위 눈이 동일하게 나왔습니다.")

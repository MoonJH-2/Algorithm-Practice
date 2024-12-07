# 대소문자 구분 없이 계산
# 알파뱃 등장 횟수 계산
# 최빈값 확인
# 출력 조건

from collections import Counter

word = input().strip().upper()
counter = Counter(word)
max_count = max(counter.values())

most_common = [key for key, value in counter.items() if value == max_count]

if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])

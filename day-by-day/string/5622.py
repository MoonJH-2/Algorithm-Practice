# n -> (n+1)
# 알파벳 대문자
# 출력 단어의 각 알파벳을 다이얼하는 데 필요한 총 시간.
def calculate_dial_time(word):
    dial = {
        'A': 2, 'B': 2, 'C': 2,
        'D': 3, 'E': 3, 'F': 3,
        'G': 4, 'H': 4, 'I': 4,
        'J': 5, 'K': 5, 'L': 5,
        'M': 6, 'N': 6, 'O': 6,
        'P': 7, 'Q': 7, 'R': 7, 'S': 7,
        'T': 8, 'U': 8, 'V': 8,
        'W': 9, 'X': 9, 'Y': 9, 'Z': 9,
    }
    total_time = 0
    for char in word:
        total_time += dial[char] + 1
    return total_time


word = input().strip()
print(calculate_dial_time(word))
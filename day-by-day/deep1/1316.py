# seen, prev_char
# 이미 본 그룹, 이전과 비교할 prev_char
# 비교하는 for문
# 받아온 words가 seen에 있다면

# char in word
# word로 받아온 char를 가져왔는데
# 그 char가 prev_char와 다르다면
# word받아온 char이 seen에서 이미 나온 적 있는 문자인지 확인
# return False 를 줘라.
# 없었으니 seen에다가 add
# prev_char를 갱신해라.
# 아니라면 return True


# words 받아와서 카운트 +=1
def is_group_char(word):
    seen = set()
    prev_char = ''

    for char in word:
        if char != prev_char:
            if char in seen:
                return False
            seen.add(char)
        prev_char = char
    return True


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0])
    words = data[1:]
    count = 0

    for word in words:
        if is_group_char(word):
            count += 1
    print(count)

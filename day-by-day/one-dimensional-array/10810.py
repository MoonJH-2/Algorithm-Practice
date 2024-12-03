import sys

input = sys.stdin.read
data = input().splitlines()

# 첫째 줄에 N개 바구니(i,j), M번 넣기(k)
N, M = map(int, data[0].split())

baskets = [0] * N

for i in range(1, M + 1):
    start, end, ball = map(int, data[i].split())
    for j in range(start - 1, end):
        baskets[j] = ball

print(" ".join(map(str, baskets)))
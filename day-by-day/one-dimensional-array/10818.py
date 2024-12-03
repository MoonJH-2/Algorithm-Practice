import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
numbers = list(map(int, data[1].split()))

m = min(numbers)
M = max(numbers)

print(f"{m} {M}")
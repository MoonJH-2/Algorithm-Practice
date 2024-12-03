import sys

input = sys.stdin.read
data = input().splitlines()

N, X = map(int, data[0].split())
numbers = list(map(int, data[1].split()))

result = [str(num) for num in numbers if num < X]
print(" ".join(result))
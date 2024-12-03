import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
results = []
star = "*"

for i in range(1, N + 1):
    results.append(star)
    star += "*"

print("\n".join(results))

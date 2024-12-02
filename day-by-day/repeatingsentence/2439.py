import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
r = []
star = "*"

for i in range(1, N + 1):
    r.append(star.rjust(N))
    star += "*"

print("\n".join(r))
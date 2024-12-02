import sys

input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
r = []

for i in range(1, T + 1):
    A, B = map(int, data[i].split())
    C = A + B
    r.append(f"Case #{i}: {A} + {B} = {C}")
print("\n".join(r))

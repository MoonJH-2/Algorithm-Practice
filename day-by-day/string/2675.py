import sys

input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
results = []

for i in range(1, T + 1):
    R, S = data[i].split()
    R = int(R)
    P = ''.join([char * R for char in S])
    results.append(P)

print('\n'.join(results) + '\n')

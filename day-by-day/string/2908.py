import sys

input = sys.stdin.read
data = input().splitlines()

A, B = map(str, data[0].split())
rev_A = int(A[::-1])
rev_B = int(B[::-1])

result = max(rev_A, rev_B)
print(result)

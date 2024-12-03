import sys

input = sys.stdin.read
data = input().splitlines()

numbers = [int(data[i]) for i in range(9)]

m_v = max(numbers)
m_i = numbers.index(m_v)+1

print(m_v)
print(m_i)
import sys

input = sys.stdin.read
data = input().strip()

words = list(data.split())
word_count = len(words)

print(word_count)

T = int(input().strip())

results = []
for _ in range(T):
    string = input().strip()
    results.append(string[0] + string[-1])

for result in results:
    print(result)

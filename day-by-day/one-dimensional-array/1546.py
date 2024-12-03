def calculate_new_average(n, scores):
    max_score = max(scores)
    new_score = [(score / max_score) * 100 for score in scores]
    new_average = sum(new_score) / n
    return new_average


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    scores = list(map(int, data[1].split()))

    results = calculate_new_average(n, scores)

    print(f"{results:.2f}")

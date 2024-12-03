# 5*
def solve_ball_exchange(n, m, swaps):
    buckets = list(range(1, n + 1))

    for i, j in swaps:
        buckets[i - 1], buckets[j - 1] = buckets[j - 1], buckets[i - 1]

    return buckets


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().splitlines()

    n, m = map(int, data[0].split())
    swaps = [tuple(map(int, line.split())) for line in data[1:]]

    result = solve_ball_exchange(n, m, swaps)
    print(" ".join(map(str, result)))
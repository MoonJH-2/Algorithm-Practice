def reverse_basket(n, operations):
    baskets = list(range(1, n + 1))
    for i, j in operations:
        baskets[i - 1:j] = reversed(baskets[i - 1:j])
    return baskets


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().splitlines()

    n, m = list(map(int, data[0].split()))
    operations = [tuple(map(int, line.split())) for line in data]
    result = reverse_basket(n, operations)

    print(" ".join(map(str, result)))

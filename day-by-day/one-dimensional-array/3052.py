def divided_numbers(submitted_numbers):
    remainders = {num % 42 for num in submitted_numbers}
    return len(remainders)


if __name__ == "__main__":
    import sys

    input = sys.stdin.read

    submitted_numbers = list(map(int, input().splitlines()))
    count = divided_numbers(submitted_numbers)

    print(count)

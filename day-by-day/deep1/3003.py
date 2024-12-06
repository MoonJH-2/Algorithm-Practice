def count_chess(current_counts):
    correct_count = [1, 1, 2, 2, 2, 8]
    result = [correct - current for correct, current in zip(correct_count, current_counts)]
    return result


if __name__ == "__main__":
    import sys

    input = sys.stdin.read().strip()
    current_count = list(map(int, input.split()))

    result = count_chess(current_count)
    print(" ".join(map(str, result)))

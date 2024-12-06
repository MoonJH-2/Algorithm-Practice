def find_alphabet_positions(S):
    positions = [-1] * 26

    for i, char in enumerate(S):
        idx = ord(char) - ord('a')
        if positions[idx] == -1:
            positions[idx] = i

    return positions


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().strip()

    S = data
    result = find_alphabet_positions(S)

    print(" ".join(map(str, result)))

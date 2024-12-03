def find_missing_students(submitted_students):
    all_students = set(range(1, 31))

    missing_students = list(all_students - set(submitted_students))
    missing_students.sort()

    return missing_students


if __name__ == "__main__":
    import sys

    input = sys.stdin.read

    submitted_students = list(map(int, input().splitlines()))

    missing_students = find_missing_students(submitted_students)

    print(missing_students[0])
    print(missing_students[1])

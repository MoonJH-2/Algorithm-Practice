import sys

croatian_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

input_words = sys.stdin.read().strip().splitlines()

for input_word in input_words:
    for cro_alpha in croatian_alphabet:
        input_word = input_word.replace(cro_alpha, "0")
    print(len(input_word))

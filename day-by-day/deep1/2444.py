# N =5
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# 빈 공간과 별 공간이 있어야함.
N = int(input())
for i in range(1, N + 1):
    spaces = ' ' * (N - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

for i in range(N-1, 0 , -1):
    spaces = ' ' * (N - i)
    stars = '*' * (2 * i - 1)
    print(spaces+stars)
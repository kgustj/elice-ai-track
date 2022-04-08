import sys


def input():
    return sys.stdin.readline().rstrip()


# 5 5
# 1 0 1 0 1
# 1 1 1 1 1
# 0 0 1 0 0
# 0 0 0 0 0
# 1 0 1 1 0
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]
answer = int(1e9)

size_x = 1 << N
size_y = 1 << M


def check(x, y):
    global answer
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                if x & (1 << i) and y & (1 << j):
                    return
                if not (x & (1 << i)) and not (y & (1 << j)):
                    return
            else:
                if x & (1 << i) and not (y & (1 << j)):
                    return

                if not (x & (1 << i)) and y & (1 << j):
                    return

    cnt = 0

    while x:
        cnt += x % 2
        x //= 2

    while y:
        cnt += y % 2
        y //= 2

    answer = min(answer, cnt)


for i in range(size_x):
    for j in range(size_y):

        check(i, j)

if answer == int(1e9):
    print(-1)
else:
    print(answer)


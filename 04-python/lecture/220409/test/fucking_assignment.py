import sys


def input():
    return sys.stdin.readline().rstrip()


N, M, K = map(int, input().split())
data = []

for _ in range(N):
    x, y = map(int, input().split())
    data.append([y, x])

data.sort()
want_score = N * K
present_score = 0
answer = 0

for node in data:
    present_score += node[1]

for node in data:
    while want_score > present_score and node[1] != M:
        answer += node[0]
        node[1] += 1
        present_score += 1

print(answer)

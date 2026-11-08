import sys


def input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
data = []
visited = [0] * (N + 1)
cnt_3 = (K // 1000 - N) // 2
answer = 0

for i in range(N):
    a, b = map(int, input().split())

    data.append((a, i, 0))
    data.append((b, i, 1))

data.sort(reverse=True)

for dt in data:
    if visited[dt[1]]:
        continue

    if dt[2]:
        if not cnt_3:
            continue

        cnt_3 -= 1

    answer += dt[0]
    visited[dt[1]] = 1

print(answer)

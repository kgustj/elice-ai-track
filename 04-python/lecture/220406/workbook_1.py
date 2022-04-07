import sys

sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
node_status = [0] + list(map(int, input().split()))
graph = [[] for i in range(N + 1)]
cnt = [[0, 0] for i in range(N + 1)]
visited = [0] * (N + 1)

red_cnt = node_status.count(1)
blue_cnt = node_status.count(2)


def dfs(node):
    visited[node] = 1
    if node_status[node]:
        cnt[node][node_status[node] - 1] += 1

    for next in graph[node]:
        if not visited[next]:
            dfs(next)
            cnt[node][0] += cnt[next][0]
            cnt[node][1] += cnt[next][1]


for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)

    graph[b].append(a)

dfs(1)


answer = 0

for i in range(1, N + 1):
    if cnt[i][0] == red_cnt and cnt[i][1] == 0:
        answer += 1

    if cnt[i][0] == 0 and cnt[i][1] == blue_cnt:
        answer += 1

print(answer)

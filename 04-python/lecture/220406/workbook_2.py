import sys

sys.setrecursionlimit(10 ** 5)


def input():
    return sys.stdin.readline().rstrip()


def dfs(node):
    for next in graph[node]:
        tree_level[next] = tree_level[node] + 1
        dfs(next)


N, M, K = map(int, input().split())
graph = [[] for i in range(N + 1)]
tree_level = [0 for i in range(N + 1)]
parent = [0 for i in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    parent[b] = a

dfs(K)

for i in range(M):
    a, b = map(int, input().split())

    if tree_level[a] < tree_level[b]:
        a, b = b, a

    while tree_level[a] != tree_level[b]:
        a = parent[a]

    while a != b:
        a, b = parent[a], parent[b]

    print(a)

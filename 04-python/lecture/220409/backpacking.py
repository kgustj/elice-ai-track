import sys

N = int(sys.stdin.readline().rstrip())

data = []
for i in range(N):
    x, y = map(int, input().split())
    data.append((y, x))

data.sort()
answer = data[-1][0]

for dt in data[::-1]:
    answer = min(answer - dt[1], dt[0] - dt[1])

print(answer)

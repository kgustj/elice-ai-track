# 5 3
N, M = map(int, input().split())

answer = 1
cnt = 0
total = 0

while True:
    total += 2 ** cnt

    cnt += 1

    if total > N + M:
        break

    if min(N, M) >= total:
        answer += total + 1
    elif max(N, M) >= total:
        answer += min(N, M) + 1
    else:
        answer += N + M - total + 1

print(answer)

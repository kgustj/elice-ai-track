import sys
from itertools import permutations


def input():
    return sys.stdin.readline().rstrip()


# 4 3
# 1234 2 0
# 5678 1 0
# 9012 1 0
N, M = map(int, input().split())
numbers = [str(dt) for dt in range(10)]
datas = []
answers = set()


def check(s):
    for i in range(M):
        strike = ball = 0

        cnt = [0] * 10

        for idx in range(len(s)):
            cnt[int(s[idx])] += 1
            cnt[int(datas[i][0][idx])] += 1

            if s[idx] == datas[i][0][idx]:
                strike += 1

        for j in range(10):
            if cnt[j] == 2:
                ball += 1

        if not (strike == datas[i][1] and ball - strike == datas[i][2]):
            return False

    return True


for i in range(M):
    s, x, y = input().split()

    datas.append((s, int(x), int(y)))

for case in permutations(numbers, N):
    if case[0] == "0":
        continue

    tmp = "".join(case)
    if check(tmp):
        answers.add(tmp)

for dt in sorted(list(answers)):
    print(dt)

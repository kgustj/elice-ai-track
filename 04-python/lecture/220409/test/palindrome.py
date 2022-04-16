import sys


def input():
    return sys.stdin.readline().rstrip()


S = input()
for i in range(len(S)):
    tmp_str = S[0:i]
    tmp = S + tmp_str[::-1]

    if tmp == tmp[::-1]:
        print(i)
        exit()

def check(s1, s2):
    if s1 == s2:
        return True

    if len(s1) % 2:
        return False

    size = len(s1) // 2

    if check(s1[:size], s2[:size]) and check(s1[size:], s2[size:]):
        return True

    if check(s1[:size], s2[size:]) and check(s1[size:], s2[:size]):
        return True

    return False


s1 = input()
s2 = input()

if check(s1, s2):
    print(1)
else:
    print(-1)


def checkParen(p):
    """
    괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
    """
    if len(p) == 0:
        return "YES"
    elif len(p) == 1:
        return "NO"

    for i in range(len(p) - 1):
        if p[i] == "(" and p[i + 1] == ")":
            q = p[:i] + p[i + 2 :]
            return checkParen(q)

    return "NO"


def main():
    # (((())())(()())((())()))
    x = input()

    print(checkParen(x))


if __name__ == "__main__":
    main()


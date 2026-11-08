def getPower(m, n):
    """
    m^n 을 LIMIT_NUMBER로 나눈 나머지를 반환하는 함수를 작성하세요.
    """
    LIMIT_NUMBER = 1000000007

    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = getPower(m, n // 2)
        return temp ** 2 % LIMIT_NUMBER
    else:
        temp = getPower(m, (n - 1) // 2)
        return temp ** 2 * m % LIMIT_NUMBER


def main():
    # 3 4
    myList = [int(v) for v in input().split()]

    print(getPower(myList[0], myList[1]))


if __name__ == "__main__":
    main()

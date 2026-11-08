def getNearestInternal(data, m):
    # m과 가장 가까운 값 후보인 두 값을 리턴하는 함수
    if len(data) == 1:
        return (data[0], data[0])
    elif len(data) == 2:
        return (data[0], data[1])

    mid = len(data) // 2
    if data[mid] <= m:
        return getNearestInternal(data[mid:], m)
    else:
        return getNearestInternal(data[: mid + 1], m)


def getNearest(data, m):
    """
    n개의 숫자가 list로 주어지고, 숫자 m이 주어질 때, n개의 숫자 중에서 m과 가장 가까운 숫자를 반환하는 함수를 작성하세요.
    가장 가까운 값 후보인 두 값을 찾고, 더 가까운 것 반환
    """
    # value[0]: m 이하이면서 가장 가까운 값
    # value[1]: m 이상이면서 가장 가까운 값
    value = getNearestInternal(data, m)

    if m - value[0] <= value[1] - m:
        return value[0]
    else:
        return value[1]


def main():
    # 1 4 6 7 10 14 16
    # 8
    data = [int(x) for x in input().split()]
    m = int(input())

    print(getNearest(data, m))


if __name__ == "__main__":
    main()

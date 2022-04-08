import math


def getSubsum(data):
    """
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    """
    result = -math.inf
    temp = 0

    for start in range(0, len(data)):
        for end in range(start, len(data)):
            temp = 0
            for i in range(start, end + 1):
                temp += data[i]
            result = max(result, temp)

    return result


def main():
    #  1 2 -4 5 3 -2 9 -10
    data = [int(x) for x in input().split()]

    print(getSubsum(data))


if __name__ == "__main__":
    main()

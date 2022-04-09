import math


def mergeSort(data):
    """
    n개의 숫자를 합병정렬을 이용하여 정렬한 결과를 list로 반환하는 함수를 작성하세요.
    """
    if len(data) == 1:
        return data

    mid = len(data) // 2
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])

    result = []

    leftp = 0
    rightp = 0

    while leftp < len(left) or rightp < len(right):
        leftValue = left[leftp] if leftp < len(left) else math.inf
        rightValue = right[rightp] if rightp < len(right) else math.inf

        if leftValue < rightValue:
            result.append(leftValue)
            leftp += 1
        else:
            result.append(rightValue)
            rightp += 1

    return result


def main():
    # 1 5 6 2 3 8 4 9 7 10
    data = [int(x) for x in input().split()]

    print(*mergeSort(data))


if __name__ == "__main__":
    main()

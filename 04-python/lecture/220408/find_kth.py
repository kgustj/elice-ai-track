def findKth(myInput, k):
    """
    매 순간마다 k번째로 작은 원소를 리스트로 반환합니다.
    """
    result = []
    data = []

    for element in myInput:
        data.append(element)
        data.sort()
        if len(data) < k:
            result.append(-1)
        else:
            result.append(data[k - 1])

    return result


def main():
    firstLine = [int(x) for x in input("n과 k를 입력하세요 (예시:10 3): ").split()]
    myInput = [int(x) for x in input("n개의 숫자를 차례대로 입력하세요 (예시:1 9 8 5 2 3 5 6 2 10): ").split()]

    print("정렬 결과: ", *findKth(myInput, firstLine[1]))


if __name__ == "__main__":
    main()

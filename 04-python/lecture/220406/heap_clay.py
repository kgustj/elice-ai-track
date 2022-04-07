import heapq


def getMinForce(weights):
    '''
    n개의 점토를 하나로 합치기 위해 필요한 힘의 합의 최솟값을 반환하는 함수를 작성하세요.
    '''
    pq = []
    result = 0

    for w in weights:
        heapq.heappush(pq, w)

    while len(pq) > 1:
        x = heapq.heappop(pq)
        y = heapq.heappop(pq)

        temp = x + y
        result += temp

        heapq.heappush(pq, temp)

    return result


def main():
    # 4
    # 1 5 7 3
    _ = int(input())
    line = [int(x) for x in input().split()]

    print(getMinForce(line))


if __name__ == '__main__':
    main()

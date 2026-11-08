import heapq


def find_mid(nums):
    '''
    n개의 정수들을 담고 있는 배열 nums가 매개변수로 주어집니다.
    nums의 각 정수들이 차례대로 주어질 때, 매 순간마다 
    "지금까지 입력된 수 중에서 중간값"을 리스트로 저장하여 반환하세요.
    '''
    n = len(nums)

    result = []

    l = []  # 최대 힙
    r = []  # 최소 힙

    for i in range(n):
        x = nums[i]

        # l 또는 r이 비어있는 경우
        if not l or not r:
            heapq.heappush(l, -x)
        else:
            if x >= -l[0]:
                heapq.heappush(r, x)
            else:
                heapq.heappush(l, -x)

        # 두 힙의 크기를 조정
        # l과 r이 갖고 있는 자료의 개수는 같아야 하며,
        # 총 자료의 개수가 홀수라면, l이 하나 더 많이 들고있게 한다.
        while not (len(l) == len(r) or len(l) == len(r) + 1):
            # 크기 조정
            # l이 들고 있는 개수가 r의 개수보다 2개 이상이다.
            if len(l) > len(r):
                # l에서 값을 뽑아와서 r에 넣어준다.
                heapq.heappush(r, -heapq.heappop(l))
            # r이 l보다 많이 갖고 있는 경우
            else:
                heapq.heappush(l, -heapq.heappop(r))

        result.append(-l[0])

    return result


def main():
    # 10
    # 1 2 3 4 5 6 7 8 9 10
    _ = int(input())

    nums = [int(v) for v in input().split()]

    print(*find_mid(nums))


if __name__ == "__main__":
    main()

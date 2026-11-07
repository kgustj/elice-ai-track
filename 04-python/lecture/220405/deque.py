'''
함수 processOrder를 구현하세요.
'''
from collections import deque


class orderInfo:
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v


def processOrder(orders):
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 반환합니다.
    '''
    vips = deque([[i+1, o] for i, o in enumerate(orders) if o.vip == 1])
    normals = deque([[i+1, o] for i, o in enumerate(orders) if o.vip == 0])

    result = []

    # vips 없거나, normal 이 없는 케이스에 대한 예외처리
    # 첫번째 고객이 누군지
    prev_end_time = 0

    if vips[0][1].time <= normals[0][1].time:
        index, o = vips.popleft()
    else:
        index, o = normals.popleft()
    result.append(index)
    prev_end_time = o.time + o.duration

    while vips and normals:
        # 만약에 작업이 처리되고 있는데 누군가의 주문이 도착한 경우
        if prev_end_time >= vips[0][1].time:
            index, o = vips.popleft()
            prev_end_time += o.duration
        elif prev_end_time >= normals[0][1].time:
            index, o = normals.popleft()
            prev_end_time += o.duration
        else:
            # 만약 작업이 처리가 됐는데도 누군가의 주문이 도착하지 않는 경우
            if vips[0][1].time <= normals[0][1].time:
                index, o = vips.popleft()
            else:
                index, o = normals.popleft()
            prev_end_time = o.time + o.duration
        result.append(index)

    while vips:
        result.append(vips.popleft()[0])
    while normals:
        result.append(normals.popleft()[0])

    return result


def main():
    p = int(input())

    orders = []

    for _ in range(p):
        myList = [int(v) for v in input().split()]
        orders.append(orderInfo(myList[0], myList[1], myList[2]))

    print(*processOrder(orders))


if __name__ == "__main__":
    main()

import heapq


class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

    def __init__(self):
        self.data = []

    def push(self, value):
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        heapq.heappush(self.data, value)

    def pop(self):
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) > 0:
            heapq.heappop(self.data)

    def top(self):
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''
        if len(self.data) == 0:
            return -1
        else:
            return self.data[0]


def heapSort(items):
    '''
    items에 있는 원소를 heap sort하여 리스트로 반환하는 함수를 작성하세요.
    단, 이전에 작성하였던 priorityQueue를 이용하세요.
    '''
    result = []

    pq = PriorityQueue()

    for item in items:
        pq.push(item)
    for _ in range(len(items)):
        result.append(pq.top())
        pq.pop()

    return result


def main():
    # line = [int(x) for x in input().split()]
    line = [int(x) for x in "10 9 8 7 6 5 4 3 2 1".split()]

    print(*heapSort(line))


if __name__ == "__main__":
    main()

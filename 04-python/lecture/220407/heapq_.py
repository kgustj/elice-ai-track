import heapq

lst = [5, 10, 15, 25, 20, 40, 60, 100, -30]

heapq.heapify(lst)
# python의 heapq는 기본적으로 min heap
a = heapq.heappop(lst)
print(a)

heapq.heappush(lst, -100)
b = heapq.heappop(lst)  # 시간 복잡도 - O(log2(n))
print(b)

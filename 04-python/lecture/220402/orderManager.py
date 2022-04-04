'''
1. LinkedListElement 클래스를 완성하세요.
2. orderManager 클래스를 완성하세요.
'''


class LinkedListElement:
    def __init__(self, data, myPrev, myNext):
        self.data = data
        self.myPrev = myPrev
        self.myNext = myNext


class orderManager:
    def __init__(self):
        self.start = None
        self.end = None

    def addOrder(self, orderId):
        order = LinkedListElement(orderId, None, None)
        if self.start == None and self.end == None:
            self.start = order
            self.end = order
        else:
            self.end.myNext = order
            order.myPrev = self.end
            self.end = order

    def removeOrder(self, orderId):
        if self.start == None and self.end == None:
            return

        current = self.start
        while current != None:
            if current.data == orderId:
                prevElem = current.myPrev
                nextElem = current.myNext

                if prevElem != None:
                    prevElem.myNext = nextElem

                if nextElem != None:
                    nextElem.myPrev = prevElem

                if current == self.end:
                    self.end == prevElem

                if current == self.start:
                    self.start = nextElem
            current = current.myNext

    def getOrder(self, orderId):
        count = 0

        if self.start == None and self.end == None:
            return -1

        current = self.start

        while current != None:
            if current.data == orderId:
                return count + 1
            else:
                current = current.myNext
                count += 1
        return -1

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
        self.elems = {}

    def addOrder(self, orderId):
        elem = LinkedListElement(orderId, None, None)
        self.elems[orderId] = elem
        if self.start == None and self.end == None:
            self.start = elem
            self.end = elem
        else:
            self.end.myNext = elem
            elem.myPrev = self.end
            self.end = elem

    def removeOrder(self, orderId):
        if self.start == None and self.end == None:
            return

        current = self.elems[orderId]
        if self.start == current and self.end == current:
            self.start = None
            self.end = None
        elif self.start == current:
            self.start = current.myNext
            (current.myNext).myPrev = None
        elif self.end == current:
            self.end = current.myPrev
            (current.myPrev).myNext = None
        else:
            current.myPrev.myNext = current.myNext
            current.myNext.myPrev = current.myPrev

    def getOrder(self, orderId):
        count = 1

        if self.start == None and self.end == None:
            return -1

        current = self.start

        while current != None:
            if current.data == orderId:
                return count

            current = current.myNext
            count += 1
        return -1

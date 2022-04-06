from treeTraversal import preorder, inorder, postorder


class Tree:
    def __init__(self, i, l, r):
        self.index = i
        self.left = l
        self.right = r
        self.depth = 0

    def setDepth(self, depth):
        self.depth = depth

    # 재귀적으로 동작한다.
    # 새로운 노드가 현재 노드의 자식으로 추가되어야 하는 경우 -> 바로 추가
    # 그렇지 않다면 자시 자식중에 새로운 노드를 받을 수 있는 노드를 탐색
    def addNode(self, i, l, r):
        '''
        트리 내의 정점 i에 대하여 왼쪽자식을 l, 오른쪽 자식을 r로
        설정해주는 함수를 작성하세요.
        '''
        if self.index == None or self.index == i:
            self.index = i
            self.left = Tree(l, None, None) if l != None else None
            self.right = Tree(r, None, None) if r != None else None

            return True
        else:
            flag = False
            if self.left != None:
                flag = self.left.addNode(i, l, r)

            if flag == False and self.right != None:
                flag = self.right.addNode(i, l, r)

            return flag


def main():
    myTree = Tree(None, None, None)

    # 5
    # 1 2 3
    # 2 4 5
    # 3 -1 -1
    # 4 -1 -1
    # 5 -1 -1
    n = int(input())

    for _ in range(n):
        myList = [int(v) for v in input().split()]

        if myList[1] == -1:
            myList[1] = None

        if myList[2] == -1:
            myList[2] = None

        myTree.addNode(myList[0], myList[1], myList[2])

    print(*preorder(myTree))
    print(*inorder(myTree))
    print(*postorder(myTree))


if __name__ == "__main__":
    main()

from tree import Tree


def getHeight(myTree):
    '''
    myTree의 높이를 반환하는 함수를 작성하세요.
    '''
    # 루트 노드를 포함해서, 왼쪽 서브트리와 오른쪽 서브트리를 모두 포함.
    # 왼쪽, 오른쪽 서브트리의 높이를 구하고 더 높은 값에 1을 더한다.
    if myTree == None:
        return 0
    else:
        return max(getHeight(myTree.left), getHeight(myTree.right)) + 1


def main():
    myTree = Tree(None, None, None)

    # 5
    # 1 2 3
    # 2 4 5
    # 3 -1 -1
    # 4 -1 -1
    # 5 -1 -1
    n = int(input())

    for i in range(n):
        myList = [int(v) for v in input().split()]

        if myList[1] == -1:
            myList[1] = None

        if myList[2] == -1:
            myList[2] = None

        myTree.addNode(myList[0], myList[1], myList[2])

    print(getHeight(myTree))


if __name__ == "__main__":
    main()

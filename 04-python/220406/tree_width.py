from tree import Tree
'''
getWidth 함수를 작성하세요.
'''


def inorder(tree, depth):
    '''
    tree를 중위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []

    if tree.left != None:
        result += inorder(tree.left, depth + 1)

    tree.setDepth(depth)
    result.append(tree)

    if tree.right != None:
        result += inorder(tree.right, depth + 1)

    return result


def getWidth(myTree):
    '''
    myTree의 너비가 가장 넓은 레벨과 그 레벨의 너비를 반환하는 함수를 작성하세요.
    가장 넓은 레벨 l과 그 레벨의 너비 w를 튜플로 반환해야 합니다.
    반환값 형식 : (l, w)
    '''
    result = inorder(myTree, 1)

    n = len(result)

    # 정점의 개수는 1000개 이하이다. (입력 조건)
    # 깊이의 최댓값은 1000이다.

    # left[i]는 깊이가 i인 모든 노드들 중에서 가장 왼쪽에 있는 노드의 행
    # right[i]는 깊이가 i인 모든 노드들 중에서 가장 오른쪽에 있는 노드의 행
    # 어떤 깊이의 너비는 right[i] - left[i]
    left = [1001 for i in range(1001)]
    right = [-1 for i in range(1001)]
    maxDepth = 0

    for i in range(n):
        d = result[i].depth

        left[d] = min(left[d], i)
        right[d] = max(right[d], i)
        maxDepth = max(maxDepth, d)

    ansDepth = 0
    ans = 0

    for i in range(1, maxDepth + 1):
        temp = right[i] - left[i] + 1
        if ans < temp:
            ansDepth = i
            ans = temp

    return (ansDepth, ans)


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

    print(*getWidth(myTree))


if __name__ == "__main__":
    main()

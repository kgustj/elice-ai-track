from queue import Queue


def preorder(tree):
    '''
    tree를 전위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    # result에 값을 추가한다 -> 현재 노드를 방문한다
    result = []

    result.append(tree.index)

    # [루트 노드] + [왼쪽 전위순회] + [오른쪽 전위순회]
    if tree.left != None:
        result += preorder(tree.left)

    if tree.right != None:
        result += preorder(tree.right)

    return result


def inorder(tree):
    '''
    tree를 중위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []

    if tree.left != None:
        result += inorder(tree.left)

    result.append(tree.index)

    if tree.right != None:
        result += inorder(tree.right)

    return result


def postorder(tree):
    '''
    tree를 후위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []

    if tree.left != None:
        result += postorder(tree.left)

    if tree.right != None:
        result += postorder(tree.right)

    result.append(tree.index)

    return result


def BFS(tree):
    '''
    tree를 BFS(너비 우선 탐색)로 순회하여 리스트로 반환하는 함수를 작성하세요.
    '''
    q = Queue()

    q.put(tree)

    result = []

    # 더 이상 방문할 노드가 없을 때 종료
    while len(q.queue) > 0:
        cur = q.get()
        if cur == None:
            continue

        result.append(cur.index)  # 방문

        q.put(cur.left)
        q.put(cur.right)

    return result

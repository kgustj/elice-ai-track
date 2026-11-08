import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
inorder_idx = {val: idx for idx, val in enumerate(inorder)}


def find_preorder(in_s, in_e, po_s, po_e):
    if in_s > in_e or po_s > po_e:
        return
    if in_s == in_e and po_s == po_e:
        print(inorder[in_s], end=" ")
        return

    parent = postorder[po_e]
    idx = inorder_idx[parent]

    find_preorder(idx, idx, po_e, po_e)
    find_preorder(in_s, idx - 1, po_s, po_e - in_e + idx - 1)
    find_preorder(idx + 1, in_e, po_e - in_e + idx, po_e - 1)


find_preorder(0, N - 1, 0, N - 1)

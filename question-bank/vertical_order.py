# Given a graph, print the vertical order of the graph, within the same level, print from left to right

#   2
#  1 3
# 4 5 6

# Output: 4 1 2 5 3 6

from collections import defaultdict, deque
class Node:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_graph(arr):
    if not arr:
        return None
    n_arr = [Node(i) for i in arr]
    l=len(n_arr)
    for i in range(l//2):
        if 2*i+1 < l:
            n_arr[i].left=n_arr[2*i+1]
        if 2*i+2<l:
            n_arr[i].right=n_arr[2*i+2]
    return n_arr[0]

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.val)
    in_order(root.right)

def pre_order(root):
    if not root:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)

def vertical_order(root):
    d = defaultdict(list)
    l,r=0,0
    q = deque([(root,0)])
    out=[]
    while q:
        n,level=q.popleft()
        l=min(l,level)
        r=max(r,level)
        d[level].append(n.val)
        if n.left:
            q.append((n.left,level-1))
        if n.right:
            q.append((n.right,level+1))
    for i in range(l,r+1):
        out.extend(d[i])
    return out

if __name__ =='__main__':
    root = construct_graph([2,1,3,4,5,6])
    out = vertical_order(root)
    print(out)
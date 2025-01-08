# properties of trees
from pydantic import BaseModel
from typing import Any, List
from collections import deque
from sortedcontainers import SortedList


class TreeNode(BaseModel):
    n: int
    l: Any
    r: Any
    def __str__(self, level=0, prefix="Root: "):
        result = " " * (level * 4) + prefix + str(self.n) + "\n"
        if self.l is not None:
            result += self.l.__str__(level + 1, "L--- ")
        if self.r is not None:
            result += self.r.__str__(level + 1, "R--- ")
        return result

### Generic tree functions

def height(t: TreeNode)->int:
    if t is None:
        return 0
    return 1+ max(height(t.l),height(t.r))
            
def size(t: TreeNode)->int:
    if t is None:
        return 0
    return 1 + size(t.l) + size(t.r)

def post_order(t: TreeNode)->None:
    if t is not None:
        post_order(t.l)
        post_order(t.r)
        print(t.n)
def in_order(t: TreeNode)->None:
    if t is not None:
        in_order(t.l)
        print(t.n)
        in_order(t.r)
def pre_order(t: TreeNode)->None:
    if t is not None:
        print(t.n)
        pre_order(t.l)
        pre_order(t.r)

def level_order(t: TreeNode)->None:
    s=deque([t])
    while len(s)>0:
        curr = s.popleft()
        print(curr.n)
        if curr.l is not None:
            s.append(curr.l)
        if curr.r is not None:
            s.append(curr.r)

### Binary tree functions
def bottom_k(t: TreeNode,k:int)->List[int]:
    def _in_order(t,k):
        if t is not None:
            _in_order(t.l,k)
            if len(b_k)==k:
                return
            b_k.append(t.n)
            _in_order(t.r,k)
    b_k = []
    _in_order(t,k)
    return b_k

def top_k(t: TreeNode,k:int)->List[int]:
    def _in_order_rev(t,k):
        if t is not None:
            _in_order_rev(t.r,k)
            if len(t_k)==k:
                return
            t_k.append(t.n)
            _in_order_rev(t.l,k)
    t_k = []
    _in_order_rev(t,k)
    return t_k

def search(t: TreeNode, target:int)->bool:
    while t:
        if t.n == target:
            return True
        elif t.n>target:
            t = t.l
        else:
            t=t.r
    return False

def insert(x:int, t: TreeNode)->TreeNode:
    if t is None:
        return TreeNode(n=x,l=None,r=None)
    elif x > t.n:
        t.r = insert(x,t.r)
    elif x < t.n:
        t.l = insert(x,t.l)
    else:
        print(f"duplicate detected - {x}")
    return t

def delete(x: int, t: TreeNode)->TreeNode:
    def _find_min(t: TreeNode)->int:
        while t.l:
            t=t.l
        return t.n
    if t.l is None and t.r is None:
        if t.n == x:
            return None
        else:
            print(f"{x} is not found")
    elif t.l is not None and t.r is None:
        if t.n == x:
            return t.l
        elif x < t.n:
            t.l = delete(x,t.l)
        else:
            print(f"{x} is not found")
    elif t.r is not None and t.l is None:
        if t.n == x:
            return t.r
        elif x>t.n:
            t.r=delete(x,t.r)
        else:
            print(f"{x} is not found")
    else:
        if x == t.n:
            t.n = _find_min(t.r)
            t.r = delete(t.n,t.r)
        elif x < t.n:
            t.l = delete(x,t.l)
        else:
            t.r = delete(x,t.r)
    return t


# cool python library which implemented BST
class Tree:

    def __init__(self,arr:List[int]):
        # maintains a sorted list of numbers
        self.l=SortedList(arr)
    def insert(self,n:int):
        # approximately log(n)
        self.l.add(n)
    def remove(self,n:int):
        # approximately log(n)
        self.l.discard(n)

    def find(self,n:int):
        # approximately log(n)
        try:
            self.l.index(n)
            return True
        except ValueError:
            return False
    def has_element_in_range(self,low:int,high:int):
        # checks if there number in the tree within the above range
        # gets the leftest position to insert low s.t. the arr is still sorted
        pos_low = self.l.bisect_left(low)
        # gets the rightest position to insert low s.t. the arr is still sorted
        pos_high = self.l.bisect_right(high)
        # first check that pos_low is not at the right of the array
        # then check if the target pos is not in within the same 'gap' in the array
        return pos_low != len(self.l) and pos_low != pos_high

    


if __name__=='__main__':
    # a = TreeNode(n=1,l=None,r=None)
    # c = TreeNode(n=3,l=None,r=None)
    # b = TreeNode(n=2,l=a,r=c)
    # d = TreeNode(n=5,l=None,r=None)
    # f = TreeNode(n=8,l=None,r=None)
    # e = TreeNode(n=6,l=d,r=f)
    # g = TreeNode(n=4,l=b,r=e)
    # h = insert(7,g)
    # print(h)
    # i = delete(4,h)
    # print(i)
    t = Tree([1,4,7])
    print(t.has_element_in_range(2,3))
    print(t.has_element_in_range(5,8))
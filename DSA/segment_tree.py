# A segment tree is a data structure which stores information in the intermediate nodes of the tree
# It is primarily used for range queries for [left,right] indexes in log(n) time
from typing import List

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree=[0]*4*self.n
        self.construct(nums,0,self.n-1,0)
    
    def construct(self, nums:List[int],left:int,right:int,index:int) -> None:
        if left==right:
            self.tree[index]=nums[left]
            return
        mid = (left+right)//2
        # populate children
        self.construct(nums,left,mid,2*index+1)
        self.construct(nums,mid+1,right,2*index+2)
        # here, the information stored is the sum of the children nodes
        self.tree[index]=self.tree[2*index+1]+self.tree[2*index+2]


    def sum_range(self,query_left,query_right,left=0,right=None,index=0)->int:
        # [left,right] contains the information of the node in this range
        # if left==right, then it is the leaf node
        if right==None:
            right=self.n-1
        if left > query_right or right < query_left:
            return 0
        if query_left <= left and right <= query_right:
            return self.tree[index]
        mid=(left+right)//2
        return self.sum_range(query_left,query_right,left,mid,2*index+1) + self.sum_range(query_left,query_right,mid+1,right,2*index+2)
    
    def update(self,pos,val,left=0,right=None,index=0)->None:
        if right==None:
            right=self.n-1
        if left == right:
            self.tree[index]=val
            return
        mid = (left+right)//2
        if pos<=mid:
            self.update(pos,val,left,mid,2*index+1)
        else:
            self.update(pos,val,mid+1,right,2*index+2)
        self.tree[index]=self.tree[2*index+1]+self.tree[2*index+2]


if __name__ == '__main__':
    st = SegmentTree([1,2,5,7,19])
    s1 = st.sum_range(0,0)
    #print(s1)
    s2 = st.sum_range(1,5)
    #print(s2)
    st.update(0,100000)
    s3 = st.sum_range(0,1)
    print(s3)

from typing import List
import math

class heap:
    # Arr impl of heap
    # left(i) = 2i+1
    # right(i) = 2i+2
    # parent(i) = floor((i-1)/2)
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.size = len(arr)
        self.heapify()
    def __str__(self):
        if not self.arr:
            return "<empty heap>"
        resp = f'''=================
size: {self.size}
arr: {self.arr}
'''
        # Calculate the depth of the full binary tree
        depth = math.ceil(math.log2(self.size + 1))
        
        # Create a copy of the array and fill it with placeholders if necessary
        full_size = 2 ** depth - 1
        full_arr = self.arr + ["_"] * (full_size - self.size)

        result = []
        level = 0
        count = 0

        while count < full_size:
            # Calculate the number of elements on the current level
            level_size = 2 ** level
            # Select elements on the current level
            level_items = full_arr[count:count + level_size]
            # Calculate spacing
            spacing = ' ' * (2 ** (depth - level - 1) - 1)

            # Create the line with appropriate spacing
            line = spacing.join(map(str, level_items)).center(2 ** depth)
            result.append(line)

            count += level_size
            level += 1

        return resp + '\n'.join(result) + "\n=================\n"
        
    def heapify(self):
        for i in range(self.size//2,-1,-1):
            self.rebuild(i)
    def insert(self,x: int):
        # Add to end of array
        self.arr.append(x)
        # bubble up
        curr_i = self.size
        parent_i = (curr_i-1)//2
        while parent_i >= 0 and self.arr[parent_i] < self.arr[curr_i]:
            tmp = self.arr[parent_i]
            self.arr[parent_i] = self.arr[curr_i]
            self.arr[curr_i] = tmp
            curr_i = parent_i
            parent_i = (curr_i-1)//2
        self.size +=1

    def pop(self)->int:
        # swap root with last element
        largest = self.arr[0]
        self.arr[0] = self.arr[self.size-1]
        #bubble down
        self.rebuild(0)
        self.size -=1
        return largest
        
    # bubble down from root
    def rebuild(self, root):
        child_i = 2*root+1
        if child_i < self.size-1:
            right_i = child_i +1
            if self.arr[child_i] < self.arr[right_i]:
                child_i = right_i
            # bubble down
            if self.arr[root] < self.arr[child_i]:
                tmp = self.arr[root]
                self.arr[root] = self.arr[child_i]
                self.arr[child_i] = tmp
                self.rebuild(child_i)


if __name__ == '__main__':
    h = heap([10,2,3,4,5,6,7,8,9])
    print(f"insert 16")
    h.insert(16)
    print(h)
    print(f"popped: {h.pop()}")
    print(h)
    print(f"insert 1")
    h.insert(1)
    print(h)

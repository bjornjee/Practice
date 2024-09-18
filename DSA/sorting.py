from typing import List
def selection_sort(n: List[int]) -> List[int]:
    for i in range(len(n)-1,-1,-1):
        idx = i
        for j in range(i):
            if n[j] > n[idx]:
                idx = j
        tmp = n[i]
        n[i] = n[idx]
        n[idx] = tmp
    return n

def bubble_sort(n: List[int]) -> List[int]:
    for i in range(len(n)):
        is_sorted = True
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                tmp = n[j+1]
                n[j+1]=n[j]
                n[j] = tmp
                is_sorted = False
        if is_sorted:
            return n
    return n

def insertion_sort(n: List[int]) -> List[int]:
    for i in range(1, len(n)):
        next = n[i]
        j = i-1
        while j >=0 and n[j] > next:
            n[j+1] = n[j]
            j -=1
        n[j+1] = next
    return n


def quick_sort(n: List[int]) -> List[int]:
    # defining this so that logic can be customized
    def _lt(i,j) -> bool:
        return i<j
    # _partition returns the index of val n[i] 
    # where all ele on left of n[i] is _lt n[i] 
    # and all val on the right is _gt n[i]
    # it is in place
    def _partition(i,j) -> int:
        p=n[i]
        l=i
        for r in range(i+1,j+1):
            # curr less than p, add to s1
            if _lt(n[r],p):
                l+=1
                #swap 
                n[l],n[r]=n[r],n[l]
        # swap p with ele in l
        n[i],n[l]=n[l],n[i]
        return l
    # just a helper function so the main func still keep the current signature
    def _inner_quick_sort(i,j):
        if i>=j:
            return
        idx = _partition(i,j)
        _inner_quick_sort(i,idx-1)
        _inner_quick_sort(idx+1,j)
    _inner_quick_sort(0,len(n)-1)
    return n


    



if __name__ == '__main__':
    arr = [5,1,6,7,2,4,8]
    print(quick_sort(arr))
        

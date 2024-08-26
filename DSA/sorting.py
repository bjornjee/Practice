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
                


if __name__ == '__main__':
    arr = [5,1,6,7,2,4,8]
    print(insertion_sort(arr))
        

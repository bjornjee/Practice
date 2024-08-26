def binary_search(l,r,arr,t):
    while l<=r:
        curr = (l+r)//2
        i = arr[curr]
        if i ==t:
            return True
        elif i<t:
            l = curr+1
        elif i>t:
            r=curr-1
    return False

if __name__=='__main__':
    arr = [1,2,5,6,7,8,10,14,15]
    found = binary_search(0,len(arr),arr,10)
    print(found)
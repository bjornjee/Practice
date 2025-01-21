# You are given an array of array, where each subarray contains tuples (date, quantity).
# Your task is to output the total quantity of stocks each day.
# Input:
# [
#     [('5/1',100),('5/5',200),('5/8',100)], #stock A
#     [('5/1',100),('5/8',30)], #stock B
#     [('5/5',100),('5/8',400)], #stock C
# ]
# Output:
#[('5/1',200),('5/5',400),('5/8',530)]


# Method: pointer for each array, increment if current date
def stock_quantity(arr):
    max_d = '13/13'
    def _date_lte(a,b):
        a_arr = a.split('/')
        b_arr = b.split('/')
        if int(a_arr[0]) < int(b_arr[0]):
            return True
        elif int(a_arr[0]) == int(b_arr[0]):
            return int(a_arr[1]) <= int(b_arr[1])
        return False
    index_arr=[(0,len(i)) for i in arr]
    out=[]
    vis=set()
    done=False
    while not done:
        # get minimum date that is not visited
        curr=0
        # first get min date
        min_d = max_d
        for idx,args in enumerate(index_arr):
            ptr,cap=args
            d,q = arr[idx][ptr]
            if _date_lte(d,min_d):
                min_d = d
        # then, for each pointer with min date, append to out and increment
        curr_quantity =0 
        done=True
        for idx,args in enumerate(index_arr):
            ptr,cap=args
            d,q = arr[idx][ptr]
            # if any pointer is less than it's capacity, not done
            if ptr<cap-1:
                done=False
            if _date_lte(d,min_d):
                curr_quantity += q
                if ptr < cap-1:
                    index_arr[idx] = (ptr+1,cap) 
            else:
                #check previous ptr value
                if ptr>0:
                    _prev_d, _prev_q= arr[idx][ptr-1]
                    curr_quantity+= _prev_q
        out.append((min_d,curr_quantity))
    return out

if __name__ == '__main__':
    input = [
        [('5/1',100),('5/5',200),('5/6',400),('5/8',100)],
        [('5/1',100),('5/8',30)], 
        [('4/12',40),('5/5',100),('5/8',400)]
    ]
    ans = stock_quantity(input)
    print(ans)        

    
# Given an array of numbers and n, find the largest number less than n. You may reuse the elements in the array.

# Test case 1:
# A = [2,5,4] 
# n = 2411
# output=2255

def find_max_digit(arr,n_str):
    result = ''
    s= []
    for i, d in enumerate(n_str):
        #TODO: impl a better way to lookup this
        possible_digits = [a for a in arr if a<=int(d)]
        if not possible_digits:
            # decrement the last and return max
            new_possible_digits = []
            while s and len(new_possible_digits)==0:
                prev = s.pop()
                new_possible_digits = [a for a in arr if a<prev]
            #can't find, return max ele len-1 times
            if len(s) == 0 or len(new_possible_digits) ==0:
                return str(max(arr))*(len(n_str)-1)
            # able to decrement prev, fill the rest with max
            return ''.join([str(a) for a in s]) + str(max(new_possible_digits)) + str(max(arr))*(len(n_str)-1-len(s))
        max_digit = max(possible_digits)
        result += str(max_digit)
        s.append(max_digit)
        if max_digit < int(d):
            return result + str(max(arr))*(len(n_str)-i-1)
    return result


if __name__=='__main__':
    a=[2,5,4]
    n = 2411
    print(find_max_digit(a,str(n)))
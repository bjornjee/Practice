# Remove duplicate strings
# If there are duplicate adjacent strings, remove them
# Input: caabbcdea
# Output: dea

def remove_duplicate(s: str)->str:
    stack = []
    l=len(s)
    for c in s:
        skip=False
        while stack and stack[-1]==c:
            stack.pop()
            skip=True
        if not skip:
            stack.append(c)
    return ''.join(stack)

# Remove duplicate string by count
# Given a threshold, remove duplicate adjacent strings if the threshold is met
# Input: ccaabbbcde, threshold: 3
# Output: aade

def remove_duplicate_by_count(s:str, threshold:int)->str:
    stack=[]
    i=0
    while i<len(s):
        j=i+1
        while j<len(s) and s[j]==s[i]:
            j+=1
        forward = j-i
        #lookback and count stack
        k=len(stack)-1
        while stack and k>=0 and stack[k]==s[i]:
            k-=1
        backward=len(stack)-k-1
        if forward+backward >=threshold:
            for h in range(backward):
                stack.pop()
        else:
            stack.extend(s[i:j])
        i=j
    return ''.join(stack)

        


if __name__ == '__main__':
    print(remove_duplicate("abccbr"))
    print(remove_duplicate_by_count('abbcccba',3))

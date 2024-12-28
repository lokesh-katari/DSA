# this uses sliding window algorithm to find out the longestsubstring without repeating characters

def longestsubstringwithoutrepeat(s):
    charSet=set()

    # as left  pointer for the window
    l = 0
    res = 0
    #iterating through the string usign the window
    for r in range(len(s)):
        # if the character is present in the charSet then remove 
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        # else add to the charSet
        charSet.add(s[r])
        res = max(res,r-l+1)
    return res


#coming to the time complexity it has o(n) time and 0(n) space

print(longestsubstringwithoutrepeat('aaaa')) 
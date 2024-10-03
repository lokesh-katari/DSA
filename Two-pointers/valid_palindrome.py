

# the ascii values for the a-z is 97 to 122 || A-Z  is 65 to 90
# similarly for the digit 0-9 is 48 to 57
# to find the valid palindrome for any string and return true if it is else false

# Topics
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# brute force approach
def isPalindrome1( s: str) -> bool:
    res = ""
    temp = s.lower()
    print(temp,"this is temp string")
    for i in temp :
        if (i.isalnum()):
            res+=i
    
    return res == res[::-1]

# two pointer approach

def isPalindrome2( s: str) -> bool:
    left = 0
    right = len(s)-1
    s = s.lower()
    while (left < right):
        while not s[left].isalnum() and left <right:
            left +=1
        while not s[right].isalnum() and left <right:
            right -=1
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True    

print(isPalindrome2("A man, a plan, a canal: Panama"))
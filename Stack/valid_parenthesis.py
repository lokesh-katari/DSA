# TC o(n)
# SC o(n)

# using stack find whther the string given is valid or not like show the all brackets are matched
# for that we are using map and stack to solve 

# the approach would be like first we iterate through the string and if the character in string is not present
# in the map then the character is a closing one --assume that
# so we can append that in to stack and continue the loop
# and other condition is if the the stack is not empty or  the stack 's last element is not matched with the map[ character ]  then return false
# either ways we need to pop the element


#  code 

def valid_parentheses(s):
    mp = {'}':'{',']':'[',')':'('}
    stack = []

    for character in s:
        if character not in mp:
            stack.append(character)
            continue
        if not stack or stack[-1] != mp[character]:
            return False
        stack.pop()
    return not stack

print(valid_parentheses('([])'))
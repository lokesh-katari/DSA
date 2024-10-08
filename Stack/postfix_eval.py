#  we will be given a set of tokens in the postfix order an we have to evaluate it 
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6


tokens = ["4","13","5","/","+"]
def postFix(tokens):
    st=[]
    for i in tokens:
        if i == '+':
            a,b = st.pop() , st.pop()
            st.append(a+b)
        elif i == '-':
            a,b = st.pop() , st.pop()
            st.append(b-a)
        elif i == '*':
            a,b = st.pop() , st.pop()
            st.append(a*b)
        elif i == '/':
            a,b = st.pop() , st.pop()
            st.append(int(float(b)/a))
        else:
            st.append(int(i))
    return st[0]
print(postFix(tokens))
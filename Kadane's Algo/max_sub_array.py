test =[-2,1,-3,4,-1,2,1,-5,4]
# output should be 6
import sys


# the below code fails at input [-1] hence the initial value is 0 so we need to get the maxi val as sys.minvalue
# time comlexity = o(n)
# space complexity = o(1)
def max_sub_arr(arr):
    maxi = -sys.maxsize-1
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum+=arr[i]
        maxi = max(curr_sum,maxi)
        if (curr_sum < 0):
            curr_sum=0
    return maxi


#brute force approach
#TC = O(n3)
#SC = O(1)
def max_sub_arr_1(arr):
    max_sum = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            max_sum = max(max_sum,sum(arr[i:j]))
    return max_sum


print(max_sub_arr_1(test))

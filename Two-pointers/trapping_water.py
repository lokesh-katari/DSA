#  leetcode link : https://leetcode.com/problems/container-with-most-water/description//

# TC  O(n) SC o(1)

# using two pointer approach 
# for this we have to find the maximum area that water can be trapped where the contianer are in a 2d plane 
# the approach is using a two pointer to solve this solution effeciently 

def trapping_water(heights):
    right = len(heights)-1
    left = 0 
    maxArea = 0
    while(left < right):
        maxArea = max((right-left)*min(heights[left],heights[right]),maxArea)
        if(heights[left]< heights[right]):
            left+=1
        else:
            right-=1
    return maxArea

print(trapping_water([1,8,6,2,5,4,8,3,7]))

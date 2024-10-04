# the trapping water problem takes a two pointer approach by  taking left and right pointer 
# T C O(n) ,SC o(1)



def trapping_water(heights):
    right = len(heights)-1
    left = 0
    sum = 0
    left_max = heights[0]
    right_max = heights[right]
    while(left <right):
        if left_max <= right_max:
            sum += left_max - heights[left]
            left+=1
            left_max = max(left_max,heights[left])
        else:
            sum+= right_max - heights[right]
            right+=1
            right_max = max(right_max,heights[right])
    return sum 

print(trapping_water([4,2,0,3,2,5]))
# Input: height = [4,2,0,3,2,5]
# Output: 9
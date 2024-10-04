#  we need to find the target where the input array is sorted 

def two_sum(nums,target):
    right = len(nums)-1
    left = 0
    while(left <right):
        req = target - nums[left]
        if(req == nums[right]):
            return[left+1,right+1]
        if (req < nums[right]):
            right-=1
        else:
            left +=1
        
print(two_sum([2,7,11,15],9))
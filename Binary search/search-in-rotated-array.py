def search(nums, target) :
    l,r = 0,len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if (nums[mid]==target):
            return mid
        #  left portion is sorted
        if (nums[l] <= nums[mid]):
            if nums[mid] < target or target < nums[l]:
                l = mid +1
            else:
                r = mid -1
        # right portionis sorted
        else:
            if nums[mid] > target or target > nums[r]:
                r=mid-1
            else:
                l= mid +1
            
    return -1

print(search([4,5,6,7,8,1,2,3],5))
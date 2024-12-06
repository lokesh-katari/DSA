def search( nums, target) :
    i= 0
    j = len(nums)-1
    mid = (i+j)//2
    while(i<=j):
        if nums[mid]==target:
            return mid
        elif target < nums[mid]:
            j = mid -1
        else:
            i = mid+1
        mid = (i+j)//2
    return -1
print(search([1,4,6,7,8,9],6))
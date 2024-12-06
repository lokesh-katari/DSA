# binary seach on each row

nums = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
target = 11
for i in range(len(nums)):
    start=0
    j = len(nums[i]) - 1
    mid = (start+j)//2
    while(start<=j):
        if nums[i][mid] == target:
            print("true")
            break
        elif(nums[i][mid] < target):
            start = mid + 1
        else:
            j = mid - 1
        mid = (start + j)//2
    

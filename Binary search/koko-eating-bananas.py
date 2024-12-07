import math
# brute force approach to check all the minimum possible values of the k 

def minEatingSpeed(piles,h):
    k = max(piles)
    res = k
    for i in range(1,k+1):
        resultantHours = 0  
        for p in piles:
            resultantHours += math.ceil(p/i) 
            
        if(resultantHours <= h):
            res  = min(res,i)
    return res

# using binary search for the optimal finding of the eating bananas per hour 
def minEatingSpeedOptimal(piles,h):
        l,r = 1, max(piles)
        mid = (l+r)//2
        res = r
        while (l<=r):
            resultantHours = 0
            for p in piles:
                resultantHours+=math.ceil(p/mid)
            if(resultantHours <= h):
                res= min(res,mid)
                r = mid -1
            else:
                l=mid+1
            mid = (l+r)//2
        return res

piles=[30,11,23,4,20]
h=5
print(minEatingSpeed(piles,h))
print(minEatingSpeedOptimal(piles,h))
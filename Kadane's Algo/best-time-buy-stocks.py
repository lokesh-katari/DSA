# brute force approach

# TC o(n2 )
def maxPro(prices):
    maxPro = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
               if(prices[j] > prices[i]):
                    maxPro = max(prices[j]-prices[i],maxPro)
    return maxPro        


# optimal solution

def maxPro2(prices):
     maxPro = 0
     minPro = float('inf')
     for i in range(len(prices)):
          minPro = min(prices[i],minPro)
          maxPro = max(maxPro,prices[i]-minPro)
     return maxPro


prices = [7,1,5,3,6,4]
print(maxPro2(prices))
a='abab'
k=2
res  =  0 
for i in range(len(a)):
    count , maxf={},0
    for j in range(i,len(a)):
        count[a[j]] = 1 +count.get(a[j],0)
        maxf  = max(maxf,count[a[j]])
        if(j-i+1)-maxf <=k:
            res = max(res,j-i+1)
print(res)
# the above algorithm is brute force to get the longestcharacter replacement in a string 
# at first we will have an count hasmap to store all the frequencies and the max frequency variable
# ** the main logic here is to check the lenght of the sliding window - max frequency of the substrings should be less than the number of replacements
#

def optimalongestcharacterreplacement(s,k):
    maxf= 0
    l=0
    r=0
    maxlen = 0
    hashmap={}
    while(r < len(s)):
        hashmap[s[r]] = 1 + hashmap.get(s[r],0)
        maxf= max(maxf,hashmap[s[r]])
        if((r-l+1)-maxf > k):
            hashmap[s[l]]-=1
            
            l+=1
        if((r-l+1)-maxf <=k):
            maxlen = max(maxlen,r-l+1)
        r+=1
    return maxlen
print(optimalongestcharacterreplacement(a,k))
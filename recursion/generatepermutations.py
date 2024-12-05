def genp(arr,temparr):
    if(len(temparr) == len(arr)):
        print(temparr)
        return
    for i in range(len(arr)):

        if(not(boolarr[i])):
           boolarr[i]= True
           temparr.append(arr[i])
           genp(arr,temparr)
           temparr.pop()
           boolarr[i] = False
arr = [1,2,3]
ind = 0
boolarr =[False]*len(arr)
print(boolarr)
genp(arr,[])
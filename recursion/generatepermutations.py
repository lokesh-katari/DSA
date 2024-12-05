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
def genpString(str,tempstr):
    if(len(str)== len(tempstr)):
        print(tempstr)
        return
    for i in range(len(str)):
        if(not boolarr2[i]):
            boolarr2[i] = True
            tempstr+=str[i]
            genpString(str,tempstr)
            tempstr.pop()
            boolarr2[i]=False


arr = [1,2,3]
ind = 0
boolarr =[False]*len(arr)
samstr = "lokesh"
boolarr2 =[False]*len(samstr)
print(boolarr)
genp(arr,[])
genpString(samstr,"")
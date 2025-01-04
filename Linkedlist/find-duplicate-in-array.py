# the problem is trickier so we have to like remove the duplicate and there is only one duplicate element present in the list
# and we do not have to use any extra space and do that using constant space with linear time
# so here we can think of this as a linked list 
# as along with the number in an array we also have the index which we can use it find the cycle in the array
#  we are using fast ans slow pointer approach for this 
# sorted

def findDuplicate(li):
    slow=0
    fast = 0
    while True:
        slow  = li[slow]
        fast = li[li[fast]]
        if slow==fast:
            break
    # we again make the slow pointer as 0 and start the pointers at the same speed wher ethe fast pointer stops
    slow =0
    while True:
        slow = li[slow]
        fast = li[fast]
        if slow == fast:
            return slow
    

li =[1,2,3,3,3,4]
print(findDuplicate(li))

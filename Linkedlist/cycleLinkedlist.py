# to check whether the linkedlist contains cycle or not 

# for checking this there can be two ways to get them
# 1 - find it by storing all the visited nodes in the set or hashmap 
# if it presents in the revisist then we can return true else false

def cycleLinedlistHashmap(head):
    visited = set()
    temp = head
    while temp :
        if temp in visited:
            return True
        visited.add(temp)
        temp = temp.next
    return False

# 2. - we can use fast and slow pointer approadch where we intentionally use two pointers
# one is slow pointer moves a single step and other is fast pointer moves two steps 

def fastSlowLinkedListCycle(head):
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow ==fast:
            return True
    return False
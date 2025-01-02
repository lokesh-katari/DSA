class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def insertnode(val,prev):
    new = ListNode(val=val)
    prev.next = new
def printLinkedlist(head):
    temp = head
    while temp:
        print("val :",temp.val)
        temp = temp.next
li = [1,2]
head = ListNode()
temp = head
for i in li:
    insertnode(i,temp)
    temp = temp.next



# first reverse the list 
# and then traverse upto the desired node 
#  and then reverse it list and retun the previous node

def removeNthFromEnd(head,n) :
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    reversed_head = prev
    if n == 1:
        reversed_head = reversed_head.next
    else:
        temp = reversed_head
        for _ in range(n-2):
            temp = temp.next
        temp.next = temp.next.next
    prev = None
    current = reversed_head
    while current :
        next_node = current.next
        current.next = prev 
        prev = current
        current = next_node
    return prev

print(printLinkedlist(removeNthFromEnd(head,2)))
# print(removeNthFromEnd(head,2))

# the another approach is using two pointers
# we can initilise the two pointers left and right 
# right ot the head and the left to the dummy previous node
# aftr traversing to the end the right becomes null and there will be thw gap of the required gap

def removefromNode(head,n):
        dummy = ListNode(0,head)
        left = dummy
        right = head
        while n>0:
            right = right.next
            n-=1
        
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
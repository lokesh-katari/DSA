# Definition for singly-linked list.
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
li = [1,2,3,4,5]
head = ListNode()
temp = head
for i in li:
    insertnode(i,temp)
    temp = temp.next

# we need to reorder the given linkedlist as l0,ln,l1,ln-1 ,.....
# to acheive this we can simply divide the list into two halves and reverse the second list
# and then merge both lists alternatively 

def reorderList(head):
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    prev = slow.next = None
# reverse the linked list
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp
# merge the both lists alternatively
# so initialise two pointers first and the second as the starting of the two lists
    first,second = head , prev
    while second:
        temp1,temp2 = first.next,second.next
        first.next = second
        second.next = temp1
        first,second = temp1,temp2
    
print("this is the reordered list with the given conditions :")
reorderList(head)
print(printLinkedlist(head))
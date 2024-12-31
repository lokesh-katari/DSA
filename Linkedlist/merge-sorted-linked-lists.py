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

l1 = [1,2,3,4,5]
l2 = [1,3,4,7,8,9]
head = ListNode()
head2 = ListNode()
temp = head
temp2 = head2
for i in l1:
    insertnode(i,temp)
    temp = temp.next
for j in l2:
    insertnode(j,temp2)
    temp2 = temp2.next


def mergeSortedArray(l1,l2):
    newNode = ListNode()
    dummy = newNode
    while l1 and l2:
        if l1.val < l2.val:
            dummy.next  = ListNode(l1.val)
            l1 = l1.next
        else:
            dummy.next = ListNode(l2.val)
            l2 = l2.next
        dummy = dummy.next
    dummy.next = l1 or l2
    return newNode.next

newHead = mergeSortedArray(head.next,head2.next)
    # print(printLinkedlist(newNode.next))
printLinkedlist(newHead)
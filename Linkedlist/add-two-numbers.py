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

l1 = [8]
l2 = [9]
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



def addTwoNumber(l1,l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0 

        summ = v1+v2+carry
        carry = summ//10
        digit = summ%10
        curr.next = ListNode(digit)
        curr = curr.next

        if l1:
            l1 = l1.next
        else:
            l1 = None
        if l2:
            l2 = l2.next
        else:
            l2 = None
    return dummy.next
node  = addTwoNumber(head.next,head2.next)
printLinkedlist(node)
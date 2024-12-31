# for reversing a linked list
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


# for reversing a linkedlist we can simple store all the values in the stack and by iteratin over the linkedlist 
# and again chagin the valurs of the node by popping the values stored in the stack 

# st =[]
# temp = head
# while temp :
#     st.append(temp.val)
#     temp = temp.next
# temp = head
# while temp :
#     temp.val = st.pop()
#     temp = temp.next
# print("naive approack for reversing a linkd list")
# printLinkedlist(head)


# next approach is to remove the links between the 
# there should a previos node \
#  and we also have to store the  current node as the temporary node 
# and store the next node for the future purposes

# prev = None
# temp = head
# while temp :
#     front = temp.next
#     temp.next = prev
#     prev = temp
#     temp = front

# print("this is the approach by changing the points with constant space ")
# printLinkedlist(head=prev)

# recursive approach

def reverserecursively(head):
    if head == None or head.next ==None:
        return head
    newNode = reverserecursively(head.next)
    front = head.next
    front.next = head
    head.next = None
    return newNode

newhead = reverserecursively(head)
printLinkedlist(newhead)
class ListNode:
    def __init__(self, val=0, next=None,random=None):
        self.val = val
        self.next = next
        self.random = random
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



def deepcopy(head):
    nodeStore={None:None}
    temp = head
    while temp:
        nodeStore[temp] = ListNode(temp.val)
        temp = temp.next
    curr = head
    while curr:
        copy = nodeStore[curr]
        copy.next = nodeStore[curr.next]
        copy.random =nodeStore[curr.random]
        curr = curr.next
    return nodeStore[head]
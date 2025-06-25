class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def read(head:ListNode):
    current = head
    while current:
        print(current.val)
        current = current.next
        
def insert(head:ListNode, val:int) -> ListNode:
    if not head:
        return ListNode(val)
    current = head
    while current.next:
        current = current.next
    current.next = ListNode(val)
    return head

head = ListNode()

head = insert(head, 1)
head = insert(head, 2)

read(head)

def update(head, old_val, new_val):
    current = head
    while current:
        if current.val == old_val:
            current.val = new_val
            break
        current = current.next
        
update(head, 2, 3)
read(head)

def delete(head, val):
    if not head:
        return None
    
    if head.val == val:
        return head.next
    
    current = head
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
            break
        current = current.next
    return head


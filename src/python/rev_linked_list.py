class ListNode():
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def printList(head):
    temp = head
    while temp:
        print(f"({temp.val})=>",end='')
        temp = temp.next
    print()

def revList(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev

if __name__ == '__main__':
    head = ListNode(8)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    printList(head)

    printList(revList(head))

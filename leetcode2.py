class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    pass


if __name__ == "__main__":
    a = ListNode(2, ListNode(4, ListNode(3)))
    b = ListNode(5, ListNode(6, ListNode(4)))
    res = addTwoNumbers(a, b)
    while res:
        print(res.val, end=" ")
        res = res.next
    print()

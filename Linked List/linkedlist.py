class Node:

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


first = Node(1)
second = Node(2)
third = Node(3)
forth = Node(4)

first.next = second
second.next = third
third.next = forth

def printLinkedListIterative(head):

    temp = head
    while temp:
        print(temp.value)
        temp = temp.next

def printLinkedListRecursive(head):
    if not head:
        return
    
    print(head.value)
    printLinkedListRecursive(head.next)

printLinkedListRecursive(first)
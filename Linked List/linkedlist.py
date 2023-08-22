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


def mergeTwoLists(self, list1, list2):
    '''
        Create a dummy list

        Have seperate pointers on list1 and list2
        Compare both pointers
        Add the mimimum to dummy list

        move dummy list pointer
        move minimum list pointer

        check if list1 is there append it to dummy list
        check if list 2 is there append it to dummy list
        
    '''
    dummyList = Node(-1)
    dummyHead = dummyList

    while list1 and list2:
        minNode = None
        if list1.value < list2.value:
            minNode = list1
            list1 = list1.next

        else:
            minNode = list2
            list2 = list2.next
        
        dummyList.next = minNode
        dummyList = dummyList.next

    if list1:
        dummyList.next = list1
    
    if list2:
        dummyList.next = list2

    return dummyHead.next

    '''
        -1, 1, 1,
                |

        1,2,3
            |

        1,3,4
            |
    '''
    
class Node:

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

def getNumberOfPeopleInfrontOfMe(val):
    
    if val == 0:
        return 0
    
    result = 1
    ret = getNumberOfPeopleInfrontOfMe(val-1)
    # print(result)
    return result+ret


def stringReversal(s, cur) -> str:

    if cur == len(s):
        return ""
    
    return stringReversal(s, cur+1) + s[cur]

def isPalindrome(s) -> bool:

    if len(s) < 2:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return isPalindrome(s[1:len(s)-1])


# print(isPalindrome("kkayyyakkk"))

def decimalToBinary(number) -> str:

    if number < 2:
        return str(number)
    
    remainder = number%2
    quotient = decimalToBinary(number//2)
    
    return str(quotient) + str(remainder)


def sumOfNaturalNumbers(number, result) -> int:

    if number == 0:
        return result
    
    result = number + result
    
    return sumOfNaturalNumbers(number-1, result)


def binarySearch(left, right, target, array):

    if left > right:
        return -1

    middle = (left+right)//2
    
    if array[middle] == target:
        return middle
    
    if array[middle] > target:
        return binarySearch(left, middle-1, target, array)
    
    else:
        return binarySearch(middle+1, right, target, array)

# arr = [1,2,3,4,5]
# print(binarySearch(0, len(arr)-1, 1, arr))


#0112358
count = [0]
def fibonacci(number, dict = {}) -> str:
    count[0] += 1
    # if number in dict:
    #     return dict[number]
    
    if number < 2:
        return number
    
    dict[number] = fibonacci(number-1) + fibonacci(number-2)
    return dict[number]

# print(fibonacci(100), count[0])

# def mergeSort(arr):

def mergeSortUtil(arr, left, right):

    if left == right:
        return
    
    middle = (left+right)//2
    mergeSortUtil(arr, left, middle)
    mergeSortUtil(arr, middle+1, right)
    merge(arr, left, middle, right)

def merge(arr, left, middle, right):

    leftArr = arr[left:middle+1]
    rightArr = arr[middle+1:right+1]
    leftPtr = 0
    rightPtr = 0

    current = left

    while leftPtr < len(leftArr) and rightPtr < len(rightArr):
        
        if leftArr[leftPtr] < rightArr[rightPtr]:
            arr[current] = leftArr[leftPtr]
            leftPtr += 1
        
        else:
            arr[current] = rightArr[rightPtr]
            rightPtr += 1

        current += 1

    while leftPtr < len(leftArr):
        arr[current] = leftArr[leftPtr]
        current += 1
        leftPtr += 1

    while rightPtr < len(rightArr):
        arr[current] = rightArr[rightPtr]
        current += 1
        rightPtr += 1
    
# arr = [5,4,3,2,1,6,9,8,7]
# print(arr)
# mergeSortUtil(arr, 0, len(arr)-1)
# print(arr)

def reverseLinkedList(head):

    if not head or not head.next:
        return head

    newHead = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None

    return newHead




# first = Node(1)
# second = Node(2)
# third = Node(3)
# forth = Node(4)

# first.next = second
# second.next = third
# third.next = forth

def printLinkedListRecursive(head):
    if not head:
        return
    
    print(head.value)
    printLinkedListRecursive(head.next)

# newFirst = reverseLinkedList(first)
# printLinkedListRecursive(newFirst)


def mergeTwoSortedList(listA, listB):

    if not listA:
        return listB
    
    if not listB:
        return listA
    
    if listA.value < listB.value:
        listA.next = mergeTwoSortedList(listA.next, listB)
        return listA

    else:
        listB.next = mergeTwoSortedList(listA, listB.next)
        return listB
    

listA1 = Node(1)
listA3 = Node(3, listA1)
listA5 = Node(5, listA3)

listB2 = Node(2)
listB4 = Node(4, listB2)
listB6 = Node(6, listB4)

# printLinkedListRecursive(mergeTwoSortedList(listA1, listB2))

def dfs(root, target):

    if not root:
        return False
    
    if root.val == target:
        return True
    
    result = False
    for neighbour in root.neighbours:
        result = result or dfs(neighbour, target)

    return result




'''
    Striver Playlist
'''

def printNameNTimes(name, count):

    if count == 0:
        return
    
    print(count, name)
    printNameNTimes(name, count-1)

def print1toN(N, currentCount=1):
    if N == 0:
        return
    print1toN(N-1)
    print(N)

def sumOfFirstNNumbers(N):
    if N == 0:
        return 0
    
    return N + sumOfFirstNNumbers(N-1)

'''
[1,2,3,4,5] == [5,4,3,2,1]
'''

def reverseAnArray(currentPointer, array):
    if currentPointer == len(array)//2:
        return
    
    array[currentPointer], array[len(array)-currentPointer-1] = array[len(array)-currentPointer-1], array[currentPointer]
    reverseAnArray(currentPointer+1, array)

def printAllSubsequence(currentPointer, array, currentSequence = ""):

    if currentPointer >= len(array):
        print(currentSequence)
        return

    printAllSubsequence(currentPointer+1, array, currentSequence)
    printAllSubsequence(currentPointer+1, array, currentSequence+str(array[currentPointer]))

    '''
        [1, 2, 3]

        []
        [3]
    '''

def printAllSubsequenceWithTarget(currentPointer, array, target, currentSequence =[]):


    if target == 0:
        return 1
    
    if target < 0 or currentPointer >= len(array):
        return 0
    count = 0
    count += printAllSubsequenceWithTarget(currentPointer+1, array, target, currentSequence)
    currentSequence.append(array[currentPointer])
    count += printAllSubsequenceWithTarget(currentPointer+1, array, target-array[currentPointer], currentSequence)
    currentSequence.pop()
    return count

subsequence = [1,2,1,2]
target = 2


# print(printAllSubsequenceWithTarget(0, subsequence, target))
# print(array)

def permute(nums):

    res = []
    pemuteUtil(nums, 0, res)
    return res

def pemuteUtil(nums, startingIndex, res):

    if startingIndex >= len(nums):
        res.append(nums.copy())
        return

    '''
        Placing every element on the first starting index
        and incresing the starting index

        This will give us all pemutations because at each index
        their can be any element
    '''
    for index in range(startingIndex, len(nums)):
        nums[startingIndex], nums[index] = nums[index], nums[startingIndex]
        pemuteUtil(nums, startingIndex+1, res)
        nums[startingIndex], nums[index] = nums[index], nums[startingIndex]

print(permute([1,2,3]))

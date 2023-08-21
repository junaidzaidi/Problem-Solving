#User function Template for python3

'''
Subset Sum - Geeks for Geeks
https://practice.geeksforgeeks.org/problems/subset-sums2234/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
'''


def subsetSums(arr):
    res = []
    subsetSumUtil(arr, 0, 0, res)
    res.sort()
    return res

def subsetSumUtil(arr, currentIndex, currentSum, res):
    if currentIndex == len(arr):
        # Once current index reaches out of bound append the result.
        res.append(currentSum)
        return
    
    # Picking up the element
    subsetSumUtil(arr, currentIndex+1, currentSum, res)
    
    # Not picking up the element
    subsetSumUtil(arr, currentIndex+1, currentSum+arr[currentIndex], res)


# print(subsetSums([5, 2, 1]))
print(2//3)

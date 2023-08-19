
def subsetsWithDup(nums):
    nums.sort()
    res = []
    subsetUtil(nums, 0, [], res)
    return res

def subsetUtil(nums, startIndex, currentSelection, res):

    res.append(currentSelection)

    # For every index pick - not pick
    for index in range(startIndex, len(nums)):

        # If the element is duplicate don't consider
        if index > startIndex and nums[index-1] == nums[index]:
            continue

        currentSelection.append(nums[index])
        subsetUtil(nums, index+1, currentSelection.copy(), res)
        currentSelection.pop()
    
print(subsetsWithDup([1,2,2,1]))
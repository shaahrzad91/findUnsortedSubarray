def findUnsortedSubarray(self, nums):

    sorted_nums=sorted(nums)
    if sorted_nums==nums:
        return 0  
    left=0
    n=len(nums)
    right=n-1
    while left<n and nums[left]==sorted_nums[left]:
        left+=1
    while right>=0 and nums[right]==sorted_nums[right]:
        right-=1
    return right-left+1


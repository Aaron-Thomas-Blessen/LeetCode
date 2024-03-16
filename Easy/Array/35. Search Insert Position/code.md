class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(target>nums[-1]):
            return len(nums)
        else:
            for i in nums:
                if(target<=i):
                    output=nums.index(i)
                    return output
                    break

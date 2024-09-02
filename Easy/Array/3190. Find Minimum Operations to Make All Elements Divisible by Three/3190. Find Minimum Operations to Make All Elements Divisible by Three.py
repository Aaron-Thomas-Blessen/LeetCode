class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        output=0
        for i in range (len(nums)):
            if (nums[i]%3 != 0):
                output+=1
        return output

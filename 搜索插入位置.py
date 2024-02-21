class Solution:


    def searchInsert(self, nums: list[int], target: int) -> int:

        for i in range (0 , len(nums)):
            if nums[i] == target :
                return i
            
        for i in range (0 , len(nums)):
            if nums[i] <= target:
                return i+1

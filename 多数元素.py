class Solution:


    def majorityElement(self, nums: list[int]) -> int:

        nums_tow = list(set(nums))
        
        nums_len = len(nums)

class Solution(object):

    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range (0, len(nums)):
            Index = []
            for j in range (1, len(nums)):
                if nums[i] + nums[j] == target:
                    if nums[i] == nums[j]:
                        order = [i]
                        return order
                    else:
                        order = [i,j]
                        return order
                else:
                    continue

nums = [3,3]
target = 6
index = Solution().twoSum(nums,target)
print(index)
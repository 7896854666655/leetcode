class Solution:


    def removeDuplicates(self, nums: list[int]) -> int:

        i,j,y= 0,0,0
        index = []
        setnum = set(nums)
        while i<len(setnum):
            j,y= 0,0
            index = []
            while j+i+1<len(nums):
                if nums[i] == nums[j+i+1]:
                    index.append(j+i+1)
                    j += 1
                else:
                    j+=1
            while y<len(index):
                del nums[index[y]-y]
                print(nums)
                y += 1        
            i+=1
nums = [1,1,1,1,1,2,2,2,2,2,3,3,3,5,3,5,3,4,4,4,4,]
Solution().removeDuplicates(nums)
            
            

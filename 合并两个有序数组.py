class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_len, nums2_len, i = len(nums1), len(nums2), 0

        nums1_index, nums2_index = 0, 0
        num = []

        num_len = nums1_len + nums2_len

        while i < num_len:
            if nums1[nums1_index] < nums2[nums2_index]:
                num.append(nums1[nums1_index])
                nums1_index += 1
                i += 1

                if nums1_index == nums1_len:

                    while nums2_index < nums2_len:
                        num.append(nums2[nums2_index])
                        nums2_index += 1
                    
                    i += num_len

            else:
                num.append(nums2[nums2_index])
                nums2_index += 1
                i += 1


                if nums2_index == nums2_len:

                    while nums1_index < nums1_len:
                        num.append(nums1[nums1_index])
                        nums1_index += 1
                    
                    i = num_len

        nums1 = num

        return nums1

'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        id, id1, id2 = m + n - 1, m - 1, n - 1
        while id1 >= 0 and id2 >= 0:
            if nums1[id1] < nums2[id2]:
                nums1[id] = nums2[id2]
                id2 -= 1
            else:
                nums1[id] = nums1[id1]
                id1 -= 1
            id -= 1
        while id2 >= 0:
            nums1[id] = nums2[id2]
            id -= 1
            id2 -= 1
'''

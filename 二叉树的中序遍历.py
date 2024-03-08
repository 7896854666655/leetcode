# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        cur_node = root

        ans = []

        if cur_node is None:
            return []
        
        ans.append(cur_node.val)

        Solution().inorderTraversal(cur_node.left)
        
        Solution().inorderTraversal(cur_node.right)
        
        return ans


        

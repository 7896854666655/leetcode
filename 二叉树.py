node_list = [
   {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
   {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
   {'data': 'D', 'left': 'H', 'right': 'I', 'is_root': False},
   {'data': 'E', 'left': 'J', 'right': None, 'is_root': False},
   {'data': 'H', 'left': None, 'right': None, 'is_root': False},
   {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
   {'data': 'F', 'left': None, 'right': None, 'is_root': False},
   {'data': 'G', 'left': None, 'right': None, 'is_root': False},
   {'data': 'I', 'left': None, 'right': None, 'is_root': False},
   {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]

class Node:
  """二叉树节点类"""
  def __init__(self, item: int,left=None,right=None):
    self.item: int = item        # 节点值
    self.left: Node | None = left # 左子节点引用
    self.right: Node | None = right # 右子节点引用
    
class Tree(object):
  def __init__(self, root=None):
    self.root = root

  def install_data(self,node_list):
    node_dict = {}
    for n in node_list:
        node = Node(n['data'], n['left'], n['right'])
        node_dict[n['data']] = node

    for n in node_list:
        node = node_dict[n['data']]
        if node.left:
            node.left = node_dict[node.left]
        if node.right:
            node.right = node_dict[node.right]

        if n['is_root']:
            self.root = node

class Solution:
    def inorderTraversal(self, tree) -> list[int]:
        
        cur_node = tree

        ans = []
        
        ans.append(cur_node)

        Solution().inorderTraversal(cur_node.left)
        
        Solution().inorderTraversal(cur_node.right)
        
        return ans

if __name__ == '__main__':
    tree = Tree()

    print(Solution().inorderTraversal(tree.install_data(node_list)))
# https://leetcode.com/problems/binary-tree-paths/description/
import TreeNode
from typing import Optional, List


class BinaryTreePaths:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        my_list: List[str] = []
        self.dfs(root, my_list, '')
        return my_list

    def dfs(self, root: Optional[TreeNode], list: List[str], partial: str):
        if root.left is None and root.right is None:
            list.append(partial + str(root.val))
            return
        if root.left is not None:
            self.dfs(root.left, list, partial + str(root.val) + '->')
        if root.right is not None:
            self.dfs(root.right, list, partial + str(root.val) + '->')


btp = BinaryTreePaths()
t = BinaryTreePaths()
tree = TreeNode.TreeNode(1)
tree.left = TreeNode.TreeNode(2)
tree.right = TreeNode.TreeNode(3)
tree.right.left = TreeNode.TreeNode(5)
result = btp.binaryTreePaths(tree)
print(result)

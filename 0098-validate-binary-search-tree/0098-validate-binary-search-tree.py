# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, maximum, minimum):
            if not node:
                return True

            if node.val <= minimum or node.val >= maximum:
                return False

            return dfs(node.left, node.val, minimum) and dfs(node.right, maximum, node.val)

        return dfs(root, float('inf'), -float('inf'))
        
    

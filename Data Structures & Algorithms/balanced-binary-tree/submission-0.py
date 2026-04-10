# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        result = [True]
        def dfs(node):
            if not node:
                return 0

            
            left = dfs(node.left)
            right = dfs(node.right)
            #print("LEFT",left,'RIGHT',right)
            if not -1 <= left-right <= 1:
                result[0] = False
            return 1 + max(left,right)
        dfs(root)
        return result[0]
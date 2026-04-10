class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = [True]
        def dfs(tree1,tree2):
            if not tree1 and not tree2:
                return
            if not tree1 or not tree2 or tree1.val != tree2.val:
                result[0] = False
                return
            dfs(tree1.left,tree2.left)
            dfs(tree1.right,tree2.right)

        dfs(p,q)
        return result[0]
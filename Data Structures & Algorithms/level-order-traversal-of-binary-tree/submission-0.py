# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        result = []
        q.append(root)
        if not root:
            return []
        while q:
            
            # run the whole current queue length and pop
            length = len(q)
            tempArr = []
            for i in range(length):
                tempNode = q.popleft()
                if tempNode:
                    tempArr.append(tempNode.val)
                    if tempNode.left:
                        q.append(tempNode.left)
                    if tempNode.right:
                        q.append(tempNode.right)
            result.append(tempArr)
        return result
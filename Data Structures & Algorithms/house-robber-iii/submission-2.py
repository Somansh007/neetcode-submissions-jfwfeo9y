# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return (0, 0)

            leftRob, leftSkip = dfs(node.left)
            rightRob, rightSkip = dfs(node.right)

            robCurrent = node.val + leftSkip + rightSkip

            skipCurrent = max(leftRob, leftSkip) + \
                          max(rightRob, rightSkip)

            return (robCurrent, skipCurrent)

        return max(dfs(root))
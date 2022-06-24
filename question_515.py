"""
515. 在每个树行中找最大值
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。



示例1：



输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]
示例2：

输入: root = [1,2,3]
输出: [1,3]


提示：

二叉树的节点个数的范围是 [0,104]
-231 <= Node.val <= 231 - 1

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        if root is None:
            return result
        stack.append(root)
        stack.append(None)
        levelMax = root.val
        isEmpty = False
        while len(stack) > 1:
            tmp = stack[0]
            del stack[0]
            if tmp is None:
                if not isEmpty:
                    result.append(levelMax)
                isEmpty = True
                stack.append(None)
                continue
            if isEmpty:
                levelMax = tmp.val
            else:
                if levelMax < tmp.val:
                    levelMax = tmp.val
            isEmpty = False
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
        if not isEmpty:
            result.append(levelMax)
        return result
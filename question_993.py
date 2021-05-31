# --*-- coding:utf-8 --*--

"""
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

 

示例 1：


输入：root = [1,2,3,4], x = 4, y = 3
输出：false
示例 2：


输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true
示例 3：



输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false
 

提示：

二叉树的节点数介于 2 到 100 之间。
每个节点的值都是唯一的、范围为 1 到 100 的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cousins-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findData(self, root, x, count):
        c1 = c2 = 0
        r1 = r2 = None
        if root.left != None:
            if root.left.val == x:
                return count, root
            else:
                c1,r1 =  self.findData(root.left, x, count + 1)
        if root.right != None:
            if root.right.val == x:
                return count, root
            else:
                c2,r2 =  self.findData(root.right, x, count + 1)
        if c1 == 0:
            return c2, r2
        else:
            return c1, r1

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        count_x, fa_x = self.findData(root, x, 1)
        count_y, fa_y = self.findData(root, y, 1)
        if count_y == 0 or count_x == 0:
            return False
        if fa_x.val == fa_y.val:
            return False
        if count_x == count_y:
            return True
        return False

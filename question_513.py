"""
513.
找树左下角的值
给定一个二叉树的
根节点
root，请找出该二叉树的
最底层
最左边
节点的值。

假设二叉树中至少有一个节点。



示例
1:

输入: root = [2, 1, 3]
输出: 1
示例
2:

输入: [1, 2, 3, 4, null, 5, 6, null, null, 7]
输出: 7

提示:

二叉树的节点个数的范围是[1, 104]
-231 <= Node.val <= 231 - 1

logo
学习
题库
讨论
竞赛
求职
商店
2

题目描述
评论(652)
题解(1.1
k)
提交记录
513.
找树左下角的值
给定一个二叉树的
根节点
root，请找出该二叉树的
最底层
最左边
节点的值。

假设二叉树中至少有一个节点。



示例
1:

输入: root = [2, 1, 3]
输出: 1
示例
2:

输入: [1, 2, 3, 4, null, 5, 6, null, null, 7]
输出: 7

提示:

二叉树的节点个数的范围是[1, 104]
-231 <= Node.val <= 231 - 1
通过次数110, 972
提交次数149, 809
请问您在哪类招聘中遇到此题？
贡献者
LeetCode
513 / 2678

智能模式
连接成功
模拟面试

12345678910111213141516171819202122232425262728


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        result = root.val
        queue = []


您上次编辑到这里，代码已从您浏览器本地的临时存储中恢复了还原默认代码模版
控制台
贡献
您是
Plus
会员，可享极速判题通道
搜索题目
""""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        result = root.val
        queue = []
        queue.append(root)
        queue.append(None)
        newF = False
        while len(queue) > 1:
            p = queue[0]
            queue = queue[1:]
            if p is None:
                newF = True
                queue.append(None)
                continue
            if newF:
                result = p.val
                newF = False
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        return result
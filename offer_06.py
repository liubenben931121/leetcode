# --*-- coding:utf-8 --*--

"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。



示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reversePrint(self, head: ListNode):
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        result = [0 for i in range(n)]
        p = head
        index = -1
        while p:
            result[index] = p.val
            index -= 1
            p = p.next
        return result
# --*-- coding:utf-8 --*--

"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

 

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverse(self, head):
        result = None
        p = head
        while p:
            tmp = p.next
            p.next = result
            result = p
            p = tmp
        return result
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        l1_r = self.reverse(l1)
        l2_r = self.reverse(l2)
        l1_r_p = l1_r
        l2_r_p = l2_r
        c = 0
        while l1_r_p and l2_r_p:
            sum = l1_r_p.val + l2_r_p.val + c
            c = sum // 10
            p = ListNode(sum % 10)
            p.next = result.next
            result.next = p
            l1_r_p = l1_r_p.next
            l2_r_p = l2_r_p.next

        while l2_r_p:
            sum = l2_r_p.val + c
            c = sum // 10
            p = ListNode(sum % 10)
            p.next = result.next
            result.next = p
            l2_r_p = l2_r_p.next

        while l1_r_p:
            sum = l1_r_p.val + c
            c = sum // 10
            p = ListNode(sum % 10)
            p.next = result.next
            result.next = p
            l1_r_p = l1_r_p.next

        if c > 0:
            p = ListNode(c)
            p.next = result.next
            result.next = p
        l1 = self.reverse(l1_r)
        l2 = self.reverse(l2_r)

        return result.next

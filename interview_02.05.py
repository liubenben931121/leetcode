# --*-- coding:utf-8 --*--
"""
给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。

 

示例：

输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?

示例：

输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-lists-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

    def addTwoNumbers_reverse(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        l1_r_p = l1
        l2_r_p = l2
        c = 0
        p = result
        while l1_r_p and l2_r_p:
            sum = l1_r_p.val + l2_r_p.val + c
            c = sum // 10
            p.next = ListNode(sum % 10)
            p = p.next
            l1_r_p = l1_r_p.next
            l2_r_p = l2_r_p.next

        while l2_r_p:
            sum = l2_r_p.val + c
            c = sum // 10
            p.next = ListNode(sum % 10)
            p = p.next
            l2_r_p = l2_r_p.next

        while l1_r_p:
            sum = l1_r_p.val + c
            c = sum // 10
            p.next = ListNode(sum % 10)
            p = p.next
            l1_r_p = l1_r_p.next

        if c > 0:
            p.next = ListNode(c)
            p = p.next
        return result.next


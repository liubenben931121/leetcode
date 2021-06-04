# --*-- coding:utf-8

# 请判断一个链表是否为回文链表。
#
#  示例 1:
#
#  输入: 1->2
# 输出: false
#
#  示例 2:
#
#  输入: 1->2->2->1
# 输出: true
#
#
#  进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#  Related Topics 链表 双指针
#  👍 996 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        result = None
        while head:
            tmp = head.next
            head.next = result
            result = head
            head = tmp
        return result

    def getListLen(self, head):
        p = head
        result = 0
        while p:
            result += 1
            p = p.next
        return result

    def isPalindrome(self, head: ListNode) -> bool:
        pheand = ListNode(0, head)
        listlen = self.getListLen(head)
        step = listlen // 2
        p1 = pheand
        p = p1
        index = 0
        while index < step:
            p = p.next
            index += 1
        p2 = p.next
        p.next = None
        p1 = self.reverse(p1.next)
        if listlen % 2 == 1:
            p2 = p2.next
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        if p1 or p2:
            return False
        return True
# leetcode submit region end(Prohibit modification and deletion)

# --*-- coding:utf-8 --*--

"""
编写一个函数，检查输入的链表是否是回文的。

 

示例 1：

输入： 1->2
输出： false
示例 2：

输入： 1->2->2->1
输出： true
 

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nlen = 0
        p = head
        while p :
            nlen += 1
            p = p.next
        phead = None
        count = nlen // 2
        p = head
        index = 0
        while index < count:
            tmp = p
            p = p.next
            tmp.next = phead
            phead = tmp
            index += 1
        if nlen % 2 == 1:
            p = p.next
        while p and phead:
            if p.val != phead.val:
                return False
            p = p.next
            phead = phead.next
        if p or phead:
            return False
        return True
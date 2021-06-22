# 用一个 非空 单链表来表示一个非负整数，然后将这个整数加一。
#
#  你可以假设这个整数除了 0 本身，没有任何前导的 0。
#
#  这个整数的各个数位按照 高位在链表头部、低位在链表尾部 的顺序排列。
#
#  示例:
#
#  输入: [1,2,3]
# 输出: [1,2,4]
#
#  Related Topics 递归 链表
#  👍 71 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
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

    def plusOne(self, head: ListNode) -> ListNode:
        phead = self.reverse(head)
        p = phead
        c = 1
        while c > 0 and p:
            p.val = p.val + c
            c = p.val // 10
            p.val = p.val % 10
            p = p.next
        p = self.reverse(phead)
        if c > 0:
            head = ListNode(c, head)
        return head

# leetcode submit region end(Prohibit modification and deletion)

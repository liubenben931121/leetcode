# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#  示例 1:
#
#  给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
#  示例 2:
#
#  给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
#  Related Topics 链表
#  👍 602 👎 0


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

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head_len = 0
        p = head
        while p:
            p = p.next
            head_len += 1
        phead = ListNode(0, head)
        p1 = phead
        index = 0
        while index < head_len / 2:
            p1 = p1.next
            index += 1
        p2 = p1.next
        p1.next = None
        p2 = self.reverse(p2)
        result = ListNode()
        p = result
        p1 = head
        while p1:
            p.next = p1
            p1 = p1.next
            p = p.next
            if p2:
                p.next = p2
                p = p.next
                p2 = p2.next
        p.next = None
        return result.next


def createList(datas):
    head = ListNode()
    p = head
    for item in datas:
        tmp = ListNode(item)
        p.next = tmp
        p = p.next
    return head.next

s = Solution()
a = [1,2,3,4]
s.reorderList(createList(a))
# leetcode submit region end(Prohibit modification and deletion)

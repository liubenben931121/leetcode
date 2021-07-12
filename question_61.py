# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#
#
#  示例 2：
#
#
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#
#
#
#
#  提示：
#
#
#  链表中节点的数目在范围 [0, 500] 内
#  -100 <= Node.val <= 100
#  0 <= k <= 2 * 109
#
#  Related Topics 链表 双指针
#  👍 586 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # if k == 0 or head or head.next == null:
        #     return head
        # p = head
        # while p.next:
        #     p = p.next
        # p.next = head
        # index = 0
        # p1 = p
        # p2 = p
        # while index < k:
        #     p2 = p2.next
        #     index += 1
        #
        # while p2 != p:
        #     p1 = p1.next
        #     p2 = p2.next
        #
        # result = p1.next
        # p1.next = None
        # # return result

        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        add = (n - k) % n
        if add == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        return ret

# leetcode submit region end(Prohibit modification and deletion)

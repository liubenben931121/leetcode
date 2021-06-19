# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链
# 表节点，返回 反转后的链表 。
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
#
#  示例 2：
#
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
#
#
#
#  提示：
#
#
#  链表中节点数目为 n
#  1 <= n <= 500
#  -500 <= Node.val <= 500
#  1 <= left <= right <= n
#
#
#
#
#  进阶： 你可以使用一趟扫描完成反转吗？
#  Related Topics 链表
#  👍 923 👎 0


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

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left >= right:
            return head
        if head == None:
            return head

        phead = ListNode(0, head)
        p1 = phead
        index = 1
        while index < left and p1.next:
            p1 = p1.next
            index += 1
        p2 = p1
        while index < right and p2.next:
            p2 = p2.next
            index += 1
        p2 = p2.next
        tmp = p2.next
        p2.next = None
        self.reverse(p1.next)
        p1.next = p2
        while p2.next:
            p2 = p2.next
        p2.next = tmp
        return phead.next

def createList(datas):
    head = ListNode()
    p = head
    for item in datas:
        tmp = ListNode(item)
        p.next = tmp
        p = p.next
    return head.next

s = Solution()
a = [1,2,3,4,5]
s.reverseBetween(createList(a), 2,4)
# leetcode submit region end(Prohibit modification and deletion)

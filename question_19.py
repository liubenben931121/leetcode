# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
#  进阶：你能尝试使用一趟扫描实现吗？
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
#
#  示例 2：
#
#
# 输入：head = [1], n = 1
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：head = [1,2], n = 1
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  链表中结点的数目为 sz
#  1 <= sz <= 30
#  0 <= Node.val <= 100
#  1 <= n <= sz
#
#  Related Topics 链表 双指针
#  👍 1419 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        phead = ListNode(0,head)
        p1 = phead
        p2 = phead
        index = 0
        while index < n and p2:
            p2 = p2.next
            index += 1
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        tmp = p1.next
        p1.next = tmp.next
        tmp.next = None
        del tmp
        return phead.next

def create(datas):
    result = ListNode()
    p = result
    for item in datas:
        p.next = ListNode(item)
        p = p.next
    return result

s = Solution()
s.removeNthFromEnd(create([1,2,3,4,5]), 2)
# leetcode submit region end(Prohibit modification and deletion)

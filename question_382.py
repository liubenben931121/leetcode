# 给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。
#
#  进阶:
# 如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？
#
#  示例:
#
#
# // 初始化一个单链表 [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
#
# // getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
# solution.getRandom();
#
#  Related Topics 水塘抽样 链表 数学 随机化
#  👍 141 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getLen(self):
        result = 0
        p = self.head
        while p:
            result += 1
            p = p.next
        return result

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        index = random.randint(0, self.getLen()-1)
        i = 0
        p = self.head
        while i < index:
            i += 1
            p = p.next
        return p.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)

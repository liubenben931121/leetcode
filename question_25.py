# --*-- coding:utf-8 --*--
"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]

输入：head = [1,2,3,4,5], k = 1
输出：[1,2,3,4,5]

输入：head = [1], k = 1
输出：[1]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head):
    result = None
    p = head
    while p :
        tmp = p.next
        p.next = result
        result = p
        p = tmp
    return result, head

def reverseKGroup( head: ListNode, k: int) -> ListNode:
    p1 = head
    p2 = head
    index = 1
    result = None
    tailp = None
    while p1:
        print(p1.val)
        if index % k == 0:
            tmp = p2
            p2 = p1.next
            p1.next = None
            head, tail = reverse(tmp)
            if result == None:
                result = head
                tailp  = tail
            else:
                tailp.next = head
                tailp = tail
            p1 = p2
            index = 1
            continue
        p1 = p1.next
        index += 1
    if p2:
        tailp.next = p2
    return result

def getListList(nums):
    head = None
    p = None
    for item in nums:
        tmp = ListNode(item)
        if head == None:
            head = tmp
            p = tmp
        else:
            p.next = tmp
            p = tmp
    return head

datas = getListList([1,2,3,4,5])
datas = reverseKGroup(datas,3)
print(datas)
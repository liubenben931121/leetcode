class Node:
    nextnode = None
    val = 0
    def __init__(self,val=0, ne=None):
        self.nextnode = ne
        self.val = val

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = Node()
        self.num = 0


    def addNum(self, num: int) -> None:
        p = self.data
        while p:
            if p.nextnode:
                if p.val < num and p.nextnode.val > num:
                    tmp = Node(num)
                    tmp.nextnode = p.nextnode
                    p.nextnode = tmp
                    self.num += 1
                    return
            else:
                p.nextnode = Node(num)
                self.num += 1
                return
            p = p.nextnode

    def findMedian(self) -> float:
        if self.num == 0:
            return 0
        if self.num == 1:
            return self.data.nextnode.val
        if self.num % 2 == 0:
            mid = self.num // 2
            index = 1
            p = self.data.nextnode
            while index < mid:
                index += 1
                p = p.nextnode
            return (p.val + p.nextnode.val) / 2
        else:
            mid = self.num // 2 + 1
            index = 1
            p = self.data.nextnode
            while index < mid:
                index += 1
                p = p.nextnode
            return p.val



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(3)
param_2 = obj.findMedian()
print(param_2)
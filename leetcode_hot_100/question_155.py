class MinStack:

    def __init__(self):
        self.datas = []
        self.mind = -1

    def push(self, val: int) -> None:
        if len(self.datas) == 0:
            self.mind = val
        self.datas.insert(0, val)
        if self.mind > val:
            self.mind = val

    def pop(self) -> None:
        if len(self.datas) == 0:
            return
        if len(self.datas) == 1:
            del self.datas[0]
            return

        if self.datas[0] == self.mind:
            self.mind = self.datas[1]
            for item in self.datas[1:]:
                if self.mind > item:
                    self.mind = item
        del self.datas[0]

    def top(self) -> int:
        res = self.datas[0]
        return res

    def getMin(self) -> int:
        return self.mind


minStack = MinStack();
minStack.push(-2);
minStack.push(-2);
minStack.push(0);
minStack.top();
minStack.pop();
minStack.getMin();
minStack.pop();
minStack.getMin();
minStack.pop();
minStack.push(2);
minStack.top();
minStack.getMin()
minStack.push(2);
minStack.top();
minStack.getMin();
minStack.pop();
minStack.getMin();
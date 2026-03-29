class MinStack:

    def __init__(self):
        self.s = []
        self.minS = []

    def push(self, val: int) -> None:
        self.s.append(val)
        # if not self.minS:
        #     self.minS.append(val)
        # else:
        #     if self.minS[-1] < val:
        #         self.minS.append(self.minS[-1])
        #     else:
        #         self.minS.append(val)
        if self.minS:
            val = min(val, self.minS[-1])
        self.minS.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.minS.pop() 

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minS[-1]

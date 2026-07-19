class MinStack:

    def __init__(self):
        self._stack = []
        self._min = None

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._min == None:
            self._min = val
        else:
            self._min = min(self._min, val)
        

    def pop(self) -> None:
        val = self._stack.pop()
        if len(self._stack) == 0:
            self._min = None
        elif self._min == val:
            self._min = min(self._stack)
        return val
        

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._min
        

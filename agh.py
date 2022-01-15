class stack:
    def __init__(self):
        self.top = None
        pass

    def push(self, value):
        if self.top is None:
            elem = StackElemnet(value, None)
            self.top = elem
        else:
            elem = StackElement(value, self.top)
            self.top = elem
        pass

    def pop(self):
        if self.top is None:
        return value
        pass

    def peak(self):
        if self.top is None:
            return None
        else:
            return self.top.value

stk = stack()
stk.push(1)
stk.push(2)
stk.push(3)
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())
from collections import deque

class FreqStack:
    def __init__(self):
        self.stack = deque()
        self.frequency = deque()

    def push(self, val):
        freq = 1
        for v, f in reversed(self.stack):
            if v == val:
                freq = f + 1
                break
        self.stack.append((val, freq))
        while len(self.frequency) < freq:
            self.frequency.append(deque())
        self.frequency[freq - 1].append(val)

    def pop(self):
        val = self.frequency[-1].pop()
        if not self.frequency[-1]:
            self.frequency.pop()
        left_values = deque()
        while self.stack:
            v, f = self.stack.pop()
            if v == val:
                break
            left_values.appendleft((v, f))
        self.stack.extend(left_values)
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# print(obj.push(8))
# param_2 = obj.pop()
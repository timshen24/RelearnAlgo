class Stack:
    def __init__(self):
        self.st = []

    def push(self, x):
        self.st.append(x)

    def pop(self):
        if len(self.st) > 0:
            self.st.pop()

    def top(self):
        if len(self.st) == 0:
            return None
        return self.st[-1]

    def get_len(self):
        return len(self.st)


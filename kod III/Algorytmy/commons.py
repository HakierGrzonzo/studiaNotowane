class SimpleStackElement:
    def __init__(self, data, prev = None) -> None:
        self.data = data
        self.prev = prev

class SimpleStack:
    def __init__(self):
        self.element = None
    
    def push(self, data):
        self.element = SimpleStackElement(data, self.element)

    def pop(self):
        data = self.element.data if self.element is not None else None
        self.element = self.element.prev if self.element is not None else None
        return data

    def last(self):
        return self.element.data if self.element is not None else None


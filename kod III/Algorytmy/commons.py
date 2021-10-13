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

class RetardedList:
    def __init__(self, size):
        self._list = [None] * size
        self._size = size
        self.end = 0

    def prepend(self, data):
        for i in reversed(range(0, self.end + 1)):
            self._list[i + 1] = self._list[i]
        self.end += 1
        self._list[0] = data
    
    def append(self, data):
        self._list[self.end] = data
        self.end += 1
        return data

    def pop(self, index):
        data = self._list[index]
        self.end -= 1
        for i in range(index, self.end):
            self._list[i] = self._list[i + 1]
        return data

    def remove(self, index):
        for j in range(index, self.end):
            self._list[j] = self._list[j + 1]
        self.end -= 1

    def find(self, toFind):
        for i in range(0, self.end + 1):
            if self._list[i] == toFind:
                return i
        else:
            return None

    def __repr__(self) -> str:
        return "[{}]".format(
                ", ".join(
                    [str(x) for x in self._list[:self.end]]
                )
            )

    def __len__(self):
        return self.end + 1
        

class Queue:
    def __init__(self, size):
        self._queue = RetardedList(size)

    def push(self, data):
        self._queue.append(data)

    def pop(self):
        return self._queue.pop(0)

    def delete(self, index):
        self._queue.remove(index)

    def find(self, toFind):
        return self._queue.find(toFind)

    def __repr__(self) -> str:
        return f"Kolejka: {self._queue}"

class PrioQueue(Queue):
    def __init__(self, size):
       super().__init__(size)
    
    def prio(self, data):
        self._queue.prepend(data)

    def __repr__(self):
        return f"Prio{super().__repr__()}"

class Stack:
    def __init__(self, size):
        self._stack = RetardedList(size)

    def pop(self):
        return self._stack.pop(0)

    def push(self, data):
        return self._stack.prepend(data)

    def remove(self, index):
        return self._stack.remove(index)

    def find(self, toFind):
        return self._stack.find(toFind)

    def __repr__(self) -> str:
        return f"Stos: {self._stack}"

class LinkedListNode:
    def __init__(self, next, data):
        self.next = next
        self.data = data

class LinkedList:
    def __init__(self):
        self.first = None

    def getNode(self, index):
        i = 0
        node = self.first
        while index > i:
            i += 1
            node = node.next
        return node

    def __getitem__(self, index):
        return self.getNode(index).data

    def __setitem__(self, index, data):
        self.getNode(index).data = data

    def __delitem__(self, index):
        if index == 0:
            newFirst = self.first.next
            self.first = self.first.next
        else:
            prev = self.getNode(index - 1)
            prev.next = prev.next.next

    def append(self, item):
        if self.first is None:
            self.first = LinkedListNode(None, item)
        else:
            node = self.first
            while (next := node.next) is not None:
                node = next
            node.next = LinkedListNode(None, item)

    def __repr__(self) -> str:
        data = []
        node = self.first
        while node is not None:
            data.append(node.data)
            node = node.next
        return "Lista jednokierunkowa: [{}]".format(", ".join(
            [str(x) for x in data]
        ))


class DoubleLinkedListNode:
    def __init__(self, next, prev, data):
        self.next = next
        self.prev = prev
        self.data = data

class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        #TODO(hakiergrzonzo) ostatni element

    def getNode(self, index):
        i = 0
        node = self.first
        while index > i:
            i += 1
            node = node.next
        return node

    def __getitem__(self, index):
        return self.getNode(index).data

    def __setitem__(self, index, data):
        self.getNode(index).data = data

    def __delitem__(self, index):
        if index == 0:
            newFirst = self.first.next
            self.first = self.first.next
        else:
            node = self.getNode(index)
            node.prev.next = node.next
            node.next.prev = node.prev
            del node

    def append(self, item):
        if self.first is None:
            self.first = DoubleLinkedListNode(None, None, item)
        else:
            node = self.first
            while (next := node.next) is not None:
                node = next
            node.next = DoubleLinkedListNode(None, node, item)

    def __repr__(self) -> str:
        data = []
        node = self.first
        while node is not None:
            data.append(node.data)
            node = node.next
        return "Lista dwukierunkowa: [{}]".format(", ".join(
            [str(x) for x in data]
        ))


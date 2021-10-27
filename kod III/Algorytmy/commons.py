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
        self.head = 0

    def prepend(self, data):
        self.head -= 1
        self._list[self.head] = data
    
    def append(self, data):
        self._list[self.end] = data
        self.end += 1
        return data

    def pop(self, index):
        data = self._list[index + self.head]
        if index == 0:
            self.head += 1
            return data
        else:
            self.end -= 1
            for i in range(self.head, self.end + 1):
                self._list[i % (len(self) + 1)] = self._list[(i + 1) % (len(self) + 1)]
        return data

    def remove(self, index):
        for j in range(index + self.head, self.end):
            self._list[j] = self._list[j + 1]
        self.end -= 1

    def find(self, toFind):
        for i in range(self.head, self.end):
            if self._list[i] == toFind:
                return i - self.head
        else:
            return None

    def __repr__(self) -> str:
        return "[{}]".format(
                ", ".join(
                    [str(x) for x in (self._list[self.head:-1] if self.head < 0 else []) + (self._list[max(self.head, 0):self.end])]
                )
            )

    def __len__(self):
        return self.end - self.head
        

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
            self.first = self.first.next
        else:
            prev = self.getNode(index - 1)
            prev.next = prev.next.next

    def append(self, item):
        if self.first is None:
            new_node = LinkedListNode(None, item)
            self.first = new_node
        else:
            node = self.first
            while (next := node.next) is not None:
                node = next
            new_node = LinkedListNode(None, item)
            node.next = new_node

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
            #newFirst = self.first.next
            self.first = self.first.next
        else:
            node = self.getNode(index)
            node.prev.next = node.next
            node.next.prev = node.prev
            del node

    def append(self, item):
        if self.first is None:
            new_node = DoubleLinkedListNode(None, None, item)
            self.first = new_node
            self.last = self.first
        else:
            new_node = DoubleLinkedListNode(None, self.last, item)
            prev = self.last
            self.last = new_node
            prev.next = self.last

    def __repr__(self) -> str:
        data = []
        node = self.first
        while node is not None:
            data.append(node.data)
            node = node.next
        return "Lista dwukierunkowa: [{}]".format(", ".join(
            [str(x) for x in data]
        ))

class CyclicListElement:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CyclicList:
    def __init__(self) -> None:
        self.first = None

    def append(self, data):
        if self.first is None:
            self.first = CyclicListElement(data)
            self.first.next = self.first
        else:
            node = self.first
            # find last node
            while node.next is not self.first:
                node = node.next
            node.next = CyclicListElement(data, self.first)
    
    def _get_node(self, index):
        node = self.first
        while node.next is not self.first and index > 0:
            node = node.next
            index -= 1
        if index > 0:
            raise IndexError()
        else:
            return node
    
    def __len__(self):
        if self.first is None:
            return 0
        else:
            node = self.first
            res = 1
            while node.next is not self.first:
                node = node.next
                res += 1
            return res


    def __getitem__(self, index):
        return self._get_node(index).data

    def __setitem__(self, index, data):
        self._get_node(index).data = data

    def __delitem__(self, index):
        if index == 0:
            self.first = self.first.next
            last = self._get_node(len(self) - 1)
            last.next = self.first
        elif 0 < index < len(self):
            prev = self._get_node(index - 1)
            prev.next = self._get_node(index + 1)
        else:
            raise IndexError()

    def __repr__(self) -> str:
        return "CyclicList: [" + ", ".join([str(self._get_node(x).data) for x in range(len(self))]) + "]"

class WartownikowaLista(RetardedList):
    def find(self, toFind):
        self.append(toFind)
        i = self.head
        while self._list[i] != toFind:
            i += 1
        if i == self.end:
            return None
        else:
            self.remove(self.end)
            return i
            

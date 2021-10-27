from commons import Queue, PrioQueue, Stack, LinkedList, DoubleLinkedList, CyclicList, WartownikowaLista

queue = Queue(20)
queue.push(1)
print(queue)
queue.push(2)
print(queue)
print(queue.pop())
print(queue)
queue.push(3)
print(queue)
queue.delete(queue.find(2))
print(queue)
print(queue.pop())

prioQueue = PrioQueue(20)
prioQueue.push(1)
prioQueue.push(2)
prioQueue.push(3)
prioQueue.prio("dziekan")
prioQueue.prio("premier")
print(prioQueue)
print(prioQueue.pop())
print(prioQueue.pop())
print(prioQueue.pop())
print(prioQueue)

stack = Stack(20)
for i in range(6):
    print("Wrzucam", i)
    stack.push(i)
print(stack)
for i in range(5):
    print("Zabieram", stack.pop())
print(stack)

linkedList = LinkedList()
for i in range(6):
    linkedList.append(i)
print(linkedList)
print("linkedList[2] to:", linkedList[2])
linkedList[2] = "wow"
print("linkedList[2] to:", linkedList[2])
del linkedList[2]
print("linkedList[2] to:", linkedList[2])

linkedList = DoubleLinkedList()
for i in range(6):
    linkedList.append(i)
print(linkedList)
print("linkedList[2] to:", linkedList[2])
linkedList[2] = "wow"
print("linkedList[2] to:", linkedList[2])
del linkedList[2]
print("linkedList[2] to:", linkedList[2])

linkedList = CyclicList()
for i in range(6):
    linkedList.append(i)
print(linkedList)
print("linkedList[2] to:", linkedList[2])
linkedList[2] = "wow"
print("linkedList[2] to:", linkedList[2])
del linkedList[2]
print("linkedList[2] to:", linkedList[2])

wartownik = WartownikowaLista(8)
for i in range(6):
    wartownik.append(i)
print(wartownik)
print(wartownik.find(2))
print(wartownik)

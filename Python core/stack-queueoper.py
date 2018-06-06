class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def printStack(self):
        [print(a, end=' ') for a in enumerate(self.items)]
        print('\n')


q = queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.printStack()
q.dequeue()
q.printStack()
q.dequeue()
q.printStack()
print(q.isEmpty())
print(q.size())


# class stack:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         self.items.pop()

#     def size(self):
#         return len(self.items)

#     def printStack(self):
#         [print(a, end=' ') for a in reversed(self.items)]
#         print('\n')


# s = stack()
# print(s.isEmpty())

# s.push(2)
# s.push(5)
# s.push(2)
# s.push(5)
# s.push(2)
# s.push(5)
# s.printStack()
# s.pop()
# s.printStack()
# print(s.isEmpty())
# print(s.size())

import random

class Node :
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:  # if next node exist
            current = current.next  # move
        current.next = Node(data)

    def search(self, target):
        current = self.head
        while current.next:
            if current.data == target :
                return True
            else :
                current = current.next
        return False


    def remove(self, target):
        if self.head.data == target:
            self.head = self.head.next
            return
        current = self.head
        previous = None

        while current :
            if current.data == target:
                previous.next = current.next
                break
            previous = current
            current = current.next

    def __str__(self):
        node = self.head
        result = []
        while node is not None:
            result.append(str(node.data))  # ✅ 문자열 리스트로 변환 by chatgpt
            node = node.next
        return " -> ".join(result)  # ✅ 문자열로 변환 후 반환 by chatgpt

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []


    def enqueue(self, item):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(item)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())


    def dequeue(self):
        if len(self.s1)==0:
            raise Exception("Cannot pop from epty queue")
        return self.s1.pop()



    # def size(self)-> int :
    #     return self._size

if __name__ == "__main__" :
    # i = 0
    # while i < 20 :
    #     n = random.randint(0, 20)
    #     l.append(n)
    #     print(n, end=" ")
    #     i+=1

    # print(l)
    # l = LinkedList()
    # l.append(7)
    # l.append(-11)
    # l.append(8)
    # print(l)
    # l.remove(7)
    # print(l)

    q = Queue()
    q.enqueue(7)
    q.enqueue(-11)
    q.enqueue(8)
    # print(q.size())
    for i in range(3):
        print(q.dequeue())
    # print(q.size())
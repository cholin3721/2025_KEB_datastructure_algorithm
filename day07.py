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

if __name__ == "__main__" :
    # i = 0
    # while i < 20 :
    #     n = random.randint(0, 20)
    #     l.append(n)
    #     print(n, end=" ")
    #     i+=1

    # print(l)
    l = LinkedList()
    l.append(7)
    l.append(-11)
    l.append(8)
    print(l)
    l.remove(7)
    print(l)
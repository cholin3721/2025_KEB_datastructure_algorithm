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

    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        return "end"

if __name__ == "__main__" :
    l = LinkedList()
    l.append(7)  # head = node(7)을 가리킴
    l.append(-11)  # current = node(7) 을 가리키고, 근데 next를 가지고 있지 않으니 , node(7)의 next는  node(-11)을 가리킴
    l.append(8)  # current는 처음에 head(7)을 가리키고 이때는 node(7)은 next가 존재하니 한번돌고 current는 node(-11)을 가리킴
    # while문을돌아 node(-11).next는 None이니깐 node(-11)의 넥스트에 node(8)을 연결시킴
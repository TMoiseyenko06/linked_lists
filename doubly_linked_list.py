class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def delete(self,data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return current.data
            current = current.next
        return None


    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def traversal(self):
        print('Elements')
        for data in self:
            print(data,end=' -> ')
        print('None')
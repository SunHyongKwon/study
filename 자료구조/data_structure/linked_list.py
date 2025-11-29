class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)

# 한방향 연결리스트
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    # 삽입 method
    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pushBack(self, key):
        new_node = Node(key)

        if self.size == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
            
        self.size += 1

    def popFront(self):
        if self.size == 0:
            return None
        else:
            current = self.head
            key = current.key
            self.head = current.next
            self.size -= 1

            del current

            return key

    def popBack(self):
        if self.size == 0:
            return None
        else:
            prev = None
            current = self.head

            while current.next != None:
                prev = current
                current = current.next

            if prev == None:
                self.head = None
            else:
                prev.next = None

            key = current.key
            self.size -= 1

            del current

            return key

    
    
    

    
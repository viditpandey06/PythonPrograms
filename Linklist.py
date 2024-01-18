class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev

            last_node.next = new_node
            new_node.prev = last_node

            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break

# Example usage
dll = DoublyCircularLinkedList()
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.display()

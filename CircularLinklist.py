# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# CircularLinkedList class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the beginning of the circular linked list
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    # Display the circular linked list
    def display(self):
        if self.head is None:
            print("Circular linked list is empty")
        else:
            temp = self.head
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break

# Create a circular linked list object
clist = CircularLinkedList()

# Insert nodes into the circular linked list
clist.insert(1)
clist.insert(2)
clist.insert(3)
clist.insert(4)

# Display the circular linked list
clist.display()

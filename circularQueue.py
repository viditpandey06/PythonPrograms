class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, value):
        if (self.tail + 1) % self.k == self.head:
            print("Queue is full!")
        elif self.head == -1:
            self.head = self.tail = 0
            self.queue[self.tail] = value
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = value

    def dequeue(self):
        if self.head == -1:
            print("Queue is empty!")
        elif self.head == self.tail:
            value = self.queue[self.head]
            self.head = self.tail = -1
            return value
        else:
            value = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return value

    def display(self):
        if self.head == -1:
            print("Queue is empty!")
        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

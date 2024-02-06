class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.marked = False
        self.parent = None
        self.child = None
        self.left = self
        self.right = self

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.num_nodes = 0

    def insert(self, key):
        new_node = FibonacciHeapNode(key)
        if self.min_node is None:
            self.min_node = new_node
        else:
            self._insert_node(new_node, self.min_node)
            if new_node.key < self.min_node.key:
                self.min_node = new_node
        self.num_nodes += 1

    def _insert_node(self, node, root):
        node.left = root
        node.right = root.right
        root.right = node
        node.right.left = node

    def extract_min(self):
        min_node = self.min_node
        if min_node is not None:
            if min_node.child is not None:
                child = min_node.child
                while True:
                    next_child = child.right
                    self._insert_node(child, self.min_node)
                    child.parent = None
                    child = next_child
                    if child == min_node.child:
                        break
            min_node.left.right = min_node.right
            min_node.right.left = min_node.left
            if min_node == min_node.right:
                self.min_node = None
            else:
                self.min_node = min_node.right
                self._consolidate()
            self.num_nodes -= 1
        return min_node

    def _consolidate(self):
        max_degree = int(self.num_nodes ** 0.5) + 1
        degree_table = [None] * max_degree
        nodes = []
        current = self.min_node
        while True:
            nodes.append(current)
            current = current.right
            if current == self.min_node:
                break
        for node in nodes:
            degree = node.degree
            while degree_table[degree] is not None:
                other = degree_table[degree]
                if node.key > other.key:
                    node, other = other, node
                self._link(other, node)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = node
        self.min_node = None
        for node in degree_table:
            if node is not None:
                if self.min_node is None:
                    self.min_node = node
                else:
                    self._insert_node(node, self.min_node)
                    if node.key < self.min_node.key:
                        self.min_node = node

    def _link(self, child, parent):
        child.left.right = child.right
        child.right.left = child.left
        child.parent = parent
        if parent.child is None:
            parent.child = child
            child.left = child
            child.right = child
        else:
            self._insert_node(child, parent.child)
        parent.degree += 1
        child.marked = False

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        node.key = new_key
        parent = node.parent
        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if node.key < self.min_node.key:
            self.min_node = node

    def _cut(self, node, parent):
        node.left.right = node.right
        node.right.left = node.left
        parent.degree -= 1
        if parent.child == node:
            parent.child = node.right
        if parent.degree == 0:
            parent.child = None
        node.left = self.min_node
        node.right = self.min_node.right
        self.min_node.right = node
        node.right.left = node
        node.parent = None
        node.marked = False

    def _cascading_cut(self, node):
        parent = node.parent
        if parent is not None:
            if not node.marked:
                node.marked = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)

    def is_empty(self):
        return self.min_node is None
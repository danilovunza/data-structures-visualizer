"""
Data Structures Visualizer

Author: Danilo Vunza
Course: COSC 2436

Description:
Demonstrates fundamental data structures.
"""

from collections import deque


# ==========================
# STACK
# ==========================

class Stack:

    def __init__(self):

        self.items = []

    def push(self, value):

        self.items.append(value)

    def pop(self):

        if self.items:

            return self.items.pop()

        return None

    def display(self):

        print("\nSTACK")

        print(self.items)


# ==========================
# QUEUE
# ==========================

class Queue:

    def __init__(self):

        self.items = deque()

    def enqueue(self, value):

        self.items.append(value)

    def dequeue(self):

        if self.items:

            return self.items.popleft()

        return None

    def display(self):

        print("\nQUEUE")

        print(list(self.items))


# ==========================
# LINKED LIST
# ==========================

class Node:

    def __init__(self, data):

        self.data = data

        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    def append(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node

            return

        current = self.head

        while current.next:

            current = current.next

        current.next = new_node

    def display(self):

        print("\nLINKED LIST")

        current = self.head

        while current:

            print(
                current.data,
                end=" -> "
            )

            current = current.next

        print("None")


# ==========================
# BINARY TREE
# ==========================

class TreeNode:

    def __init__(self, value):

        self.value = value

        self.left = None

        self.right = None


class BinaryTree:

    def __init__(self):

        self.root = None

    def insert(self, value):

        if self.root is None:

            self.root = TreeNode(value)

            return

        self._insert_recursive(
            self.root,
            value
        )

    def _insert_recursive(
        self,
        node,
        value
    ):

        if value < node.value:

            if node.left is None:

                node.left = TreeNode(value)

            else:

                self._insert_recursive(
                    node.left,
                    value
                )

        else:

            if node.right is None:

                node.right = TreeNode(value)

            else:

                self._insert_recursive(
                    node.right,
                    value
                )

    def inorder(self):

        print("\nBINARY TREE")

        self._inorder_recursive(
            self.root
        )

        print()

    def _inorder_recursive(
        self,
        node
    ):

        if node:

            self._inorder_recursive(
                node.left
            )

            print(
                node.value,
                end=" "
            )

            self._inorder_recursive(
                node.right
            )


# ==========================
# HASH TABLE
# ==========================

class HashTable:

    def __init__(self):

        self.table = {}

    def insert(
        self,
        key,
        value
    ):

        self.table[key] = value

    def display(self):

        print("\nHASH TABLE")

        for key, value in self.table.items():

            print(
                f"{key}: {value}"
            )


# ==========================
# MAIN PROGRAM
# ==========================

def main():

    stack = Stack()

    queue = Queue()

    linked_list = LinkedList()

    tree = BinaryTree()

    hash_table = HashTable()

    print("=" * 60)

    print("DATA STRUCTURES VISUALIZER")

    print("=" * 60)

    stack.push("A")
    stack.push("B")
    stack.push("C")

    stack.display()

    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    queue.display()

    linked_list.append("Node1")
    linked_list.append("Node2")
    linked_list.append("Node3")

    linked_list.display()

    tree.insert(50)
    tree.insert(25)
    tree.insert(75)
    tree.insert(10)

    tree.inorder()

    hash_table.insert(
        "Student",
        "Danilo"
    )

    hash_table.insert(
        "Course",
        "COSC 2436"
    )

    hash_table.display()


main()

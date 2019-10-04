from linkedlist_node import


class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer

        print()

    def _delete(self, prev, node):
        self.length = self.length - 1
        if not prev:
            self.head = node.pointer
        else:
            prev.pointer = node.pointer

    def _add(self, value):
        self.length = self.length + 1
        self.head = Node(value, self.head)


    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = None
            node = node.pointer
            i += 1

        return node, prev, i


    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False


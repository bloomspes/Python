# DFS 에서 유용하게 사용 된다.
# node와 pointer를 활용하여 알고리즘 작성.

class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.count = self.count + 1

    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count = self.count - 1

            return node.value

        else:
            print("스택이 비어 있습니다.")

    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print("스택이 비어 있습니다.")

    def size(self):
        return self.count

    def _print_list(self):
        node = self.head

        while node:
            print(node.value, end=" ")
            node = node.pointer

if __name__ == "__main__":
    stack = Stack()

    print("스택이 비어있는지 확인 : {0}".format(stack.isEmpty()))
    print("스택에 데이터를 추가 합니다.")

    for i in range(20):
        stack.push(i)

    stack._print_list()

    print("스택 크기 : {0}".format(stack.size()))
    print("peek: {0}".format(stack.peek()))
    print("pop: {0}".format(stack.pop()))
    print("again peek: {0}".format(stack.peek()))
    stack._print_list()

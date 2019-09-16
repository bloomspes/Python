# python 으로 stack 알고리즘 구현
# append 와 pop 메소드로 구현이 가능하다.

# stack 자료 구조는 배열의 끝에서만 데이터 접근이 가능하다.
# 그런점 때문에 이를 실제로 코드에 적용할 경우 배열 인덱스 접근도 신경써야 한다.

from pip._vendor.progress.counter import Stack

class Stack(object):
    def __init__(self):
        self.items = []

    def isempty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value

        else:
            print("스택이 비어 있습니다.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]

        else:
            print("스택이 비어 있습니다.")

    def __repr__(self):
        return repr(self.items)


if __name__ == "__main__":

    stack = Stack()

    print("스택이 비어 있는지 확인: {0}".format(stack.isempty()))
    print("스택에 데이터를 추가합니다.")

    for i in range(10):
        stack.push(i)

    print("스택 크기: {0}".format(stack.size()))
    print("peek: {0}".format(stack.peek()))
    print("pop: {0}".format(stack.pop()))
    print(stack)
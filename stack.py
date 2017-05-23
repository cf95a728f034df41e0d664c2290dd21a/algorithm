
from node import Node


class Stack:
    def __init__(self):
        self._last = None

        self._len = 0

        self._current = None

    def __len__(self):
        return self._len

    def push(self, item):
        node = Node(value=item)
        
        if self._len == 0:
            self._last = node
        else:
            node.reference = self._last
            self._last = node
        
        self._len += 1

    def pop(self, **kwargs):
        if self._last:
            item = self._last.value
            self._last = self._last.reference
            self._len -= 1
        else:
            if 'default' in kwargs:
                item = kwargs['default']
            else:
                raise KeyError('pop from an empty stack')

        return item

    @property
    def last(self):
        return getattr(self._last, 'value', None)

    def __iter__(self):
        self._index = 0
        self._current = self._last
        return self

    def __next__(self):
        if not self._current:
            raise StopIteration

        item = self._current.value

        self._current = self._current.reference

        return item
    
    def __str__(self):
        return '[{}]'.format(', '.join([str(item) for item in self]))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    import random

    samples = list(range(10))
    random.shuffle(samples)

    stack = Stack()
    
    for item in samples:
        stack.push(item)
        print(stack)

    print()
    for item in stack:
        print(item, end=', ')
    print('\n')

    for item in samples:
        stack.pop()
        print(stack)


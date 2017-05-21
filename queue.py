
from node import Node


class Queue:
    def __init__(self):
        self._first = None
        self._last = None

        self._len = 0

        self._index = 0
        self._current = None

    def __len__(self):
        return self._len

    def enqueue(self, item):
        node = Node(value=item)
        
        if self._len == 0:
            self._first = node
            self._last = node
        else:
            self._last.reference = node
            self._last = node
        
        self._len += 1

    def dequeue(self, default=None):
        if self._first:
            item = self._first.value
            self._first = self._first.reference
            self._len -= 1
        else:
            item = default

        return item

    @property
    def first(self):
        return self._first

    @property
    def last(self):
        return self._last

    def __iter__(self):
        self._index = 0
        self._current = self._first
        return self

    def __next__(self):
        if self._index == self._len:
            raise StopIteration

        item = self._current

        self._current = self._current.reference
        self._index += 1

        return item
    
    def __str__(self):
        return '[{}]'.format(', '.join([str(item.value) for item in self]))


if __name__ == '__main__':
    import random

    l = list(range(10))
    q = Queue()
    
    random.shuffle(l)
    for item in l:
        q.enqueue(item)
        print(q)

    print()
    for item in q:
        print(item.value, end=', ')
    print('\n')

    for item in l:
        q.dequeue()
        print(q)

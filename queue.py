
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

    def dequeue(self, **kwargs):
        if self._first:
            item = self._first.value
            self._first = self._first.reference
            self._len -= 1
            if self._len == 0:
                self._last = None
        else:
            if 'default' in kwargs:
                item = kwargs['default']
            else:
                raise KeyError('dequeue from an empty queue')

        return item

    @property
    def first(self):
        return getattr(self._first, 'value', None)

    @property
    def last(self):
        return getattr(self._last, 'value', None)

    def __iter__(self):
        self._index = 0
        self._current = self._first
        return self

    def __next__(self):
        if self._index == self._len:
            raise StopIteration

        item = self._current.value

        self._current = self._current.reference
        self._index += 1

        return item
    
    def __str__(self):
        return '[{}]'.format(', '.join([str(item) for item in self]))

    def __repr__(self):
        return self.__str__()


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
        print(item, end=', ')
    print('\n')

    for item in l:
        q.dequeue()
        print(q)


class Node:
    def __init__(self, value, reference=None):
        self._value = value
        self._reference = reference

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference


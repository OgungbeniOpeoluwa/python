from chapter5.queue_full_capacity_exception import QueueFullCapacityException


class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self._numberOfElement = 0
        self._lists = []
        self._count = 0

    def is_empty(self):
        if self._numberOfElement == 0:
            return True

    def add(self, element):
        self.validate_capacity()
        self._numberOfElement += 1
        self._lists.append(element)

    def remove(self):
        if self._count == self._numberOfElement:
            raise QueueFullCapacityException
        result = self._lists.pop(0)
        self._count += 1
        return result

    def peek(self):
        return self._lists[0]

    def validate_capacity(self):
        if len(self._lists) == self.__capacity:
            raise QueueFullCapacityException("Queue is full")

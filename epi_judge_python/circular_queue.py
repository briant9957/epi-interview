from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.queue = [0] * capacity
        self.head = 0
        self.tail = -1
        self.qSize = 0
        return

    def enqueue(self, x: int) -> None:
        if self.qSize == len(self.queue):
            newQueue = [0] * (2 * len(self.queue))
            start = self.head
            for i in range(self.qSize):
                adjustedIndex = start % len(self.queue)
                newQueue[i] = self.queue[adjustedIndex]
                start += 1
            self.head = 0
            self.tail = self.qSize - 1
            self.queue = newQueue

        adjustedIndex = (self.tail + 1) % len(self.queue)
        self.queue[adjustedIndex] = x
        self.qSize += 1
        self.tail += 1

        return

    def dequeue(self) -> int:
        adjustedIndex = self.head % len(self.queue)
        element = self.queue[adjustedIndex]
        self.head += 1
        self.qSize -= 1

        return element

    def size(self) -> int:
        return self.qSize


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))

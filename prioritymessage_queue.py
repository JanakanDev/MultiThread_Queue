import threading
from queue import PriorityQueue

class PriorityMessageQueue:
    def __init__(self):
        self.queue = PriorityQueue()
        self.lock = threading.Lock()

    def enqueue(self, priority, message):
        with self.lock:
            self.queue.put((priority, message))

    def dequeue(self):
        with self.lock:
            if not self.queue.empty():
                return self.queue.get()[1]
            else:
                return None

    def peek(self):
        with self.lock:
            if not self.queue.empty():
                return self.queue.queue[0][1]
            else:
                return None

    def is_empty(self):
        with self.lock:
            return self.queue.empty()
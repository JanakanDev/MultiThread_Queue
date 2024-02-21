import threading
from queue import PriorityQueue
from concurrent.futures import ThreadPoolExecutor
import time
from prioritymessage_queue import PriorityMessageQueue

class ThreadWithMessageQueue(threading.Thread):
    def __init__(self, thread_id, message_queues, executor):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.message_queue = PriorityMessageQueue()
        self.message_queues = message_queues
        self.executor = executor
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            if not self.message_queue.is_empty():
                message = self.message_queue.dequeue()
                self.executor.submit(self.process_message, message)
            else:
                time.sleep(0.1)  # Sleep briefly to reduce CPU usage

    def send_message(self, receiver_id, priority, message):
        if receiver_id in self.message_queues:
            self.message_queues[receiver_id].enqueue(priority, message)
            print(f"Thread {self.thread_id} sent message to Thread {receiver_id}: {message}")

    def process_message(self, message):
        print(f"Thread {self.thread_id} received message: {message}")
        # Simulate some processing
        time.sleep(1)
        print(f"Thread {self.thread_id} processed message: {message}")

    def stop(self):
        self.stop_event.set()

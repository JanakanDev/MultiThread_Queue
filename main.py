from threadWithmessage_queue import ThreadWithMessageQueue
from prioritymessage_queue import PriorityMessageQueue
from concurrent.futures import ThreadPoolExecutor
import time


def main():
    number_of_threads = 5
    message_queues = {}
    threads = []
    executor = ThreadPoolExecutor(max_workers=10)

    # Initialize threads and their respective message queues
    for i in range(number_of_threads):
        message_queues[i] = PriorityMessageQueue()
        thread = ThreadWithMessageQueue(i, message_queues, executor)
        threads.append(thread)
        thread.start()

    # Simulate sending messages between threads
    threads[0].send_message(1, 1, "Hello from Thread 0 to Thread 1")
    threads[1].send_message(2, 2, "Hello from Thread 1 to Thread 2")
    threads[2].send_message(0, 3, "Hello from Thread 2 to Thread 0")
    threads[3].send_message(4, 1, "Hello from Thread 3 to Thread 4")
    threads[4].send_message(3, 2, "Hello from Thread 4 to Thread 3")

    time.sleep(2)  # Allow some time for messages to be processed

    # Stop threads
    for thread in threads:
        thread.stop()
    for thread in threads:
        thread.join()

    executor.shutdown()

if __name__ == "__main__":
    main()

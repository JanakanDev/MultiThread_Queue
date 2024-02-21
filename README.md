# MultiThread_Queue
This Python program demonstrates a multi-threaded priority message queue implementation using threads, a priority queue, and a thread pool.

## Purpose

The purpose of this program is to showcase how to implement a priority message queue that supports multiple threads sending messages to each other with different priorities. Each thread has its own message queue and can send messages to other threads. Upon receiving a message, the receiving thread performs a simple action concurrently using a thread pool.

## Features

- Priority message queue data structure supporting enqueue, dequeue, peek, and empty check operations.
- Thread pool with a fixed number of threads for concurrent execution of tasks.
- Sending messages between threads with specified priorities.
- Processing messages with simple actions using a thread pool.

## How to Run

1. Make sure you have Python 3.x installed on your system.
2. Clone or download the repository to your local machine.
3. Navigate to the directory containing the Python files.
4. Run the program

## Priority message queue

- `priority_message_queue.py`: Contains the implementation of the priority message queue, threads, and main program logic.
- `README.md`: This file, providing information about the program and how to run it.

## Dependencies

This program requires no external dependencies beyond the Python standard library.

## Additional Notes

- Adjust the `number_of_threads` and simulated message sending in the `main()` function based on your testing needs.
- This example demonstrates basic functionality and can be adapted for more complex scenarios or specific application requirements.

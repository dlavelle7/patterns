"""The Producer Consumer problem.

The producer and the consumer both share a fixed size queue. The producers job
is to put data in the queue and the consumers job is to take data from the
queue.

The problem is to ensure that the producer won't try to produce data when the
queue is full and the consumer won't try to consume data when the queue is
empty.
"""
import Queue
import logging
import threading

# Shared queue between producer and consumers
BUFFER_SIZE = 4
queue = Queue.Queue(BUFFER_SIZE)

# Thread safe logging to stdout
logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


class Producer(threading.Thread):

    def run(self):
        for data in xrange(10):
            # Block indefinitely, until a free slot is created by consumer
            queue.put(data)
            log.info("%s produced %s", self.name, data)


class Consumer(threading.Thread):

    def __init__(self):
        super(Consumer, self).__init__()
        # Program exits when no alive non-daemonic threads are left (default).
        # If True, exits when only daemon threads left, shutting down abruptly
        self.daemon = False

    def run(self):
        while True:
            try:
                # Wait for 2 secs and terminate if no data
                data = queue.get(block=True, timeout=2)
                log.info("%s consumed %s", self.name, data)
                queue.task_done()  # processing for this get() is over
            except Queue.Empty:
                break
        log.info("%s finished", self.name)


for p in xrange(5):
    Producer().start()


for c in xrange(10):
    Consumer().start()


queue.join()  # Main thread waits until all tasks in queue are processed
log.info("Main thread finished, no further consuming")
assert queue.qsize() == 0

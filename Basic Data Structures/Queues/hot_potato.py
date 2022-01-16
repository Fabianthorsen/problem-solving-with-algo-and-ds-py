# How the alogrithm will work:
# Take an list of names as input, and a constant num to be used for counting
# Returns the name of the very last person after repetitive counting by num
# Assume person holding potato is at the front of the queue
# When passing the potato, the simulation will dequeue and
# then enque what was dequeued. After num deq/enq, the person at the
# front will be removed. Continue until one remains in queue.

from queues import Queue
from typing import List


def hot_potato(name_lst: List[str], num: int) -> str:
    sim_queue = Queue[str]()
    for name in name_lst:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

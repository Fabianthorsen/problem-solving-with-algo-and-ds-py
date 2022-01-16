# Algorithm outline:
# 1. Create a queue of print tasks.
# Each task has a timestamp on arrival. Queue is empty to start with
# 2. For each second:
#   - Check if new task gets created. If so, add to queue with current
#   second as timestamp
#   - If printer is not busy, and task is waiting:
#       * Dequeue next task, assign to printer
#       * Subtract timestamp from current_second to compute waiting time
#       * Append waiting time to list for later processing
#       * Based on number of pages, calculate processing time required
#   - Printer does one second of processing. Subtract one from
#   time required for task.
#   - If task is completed: printer is no longer busy.
# 3. After sim is complete, compute average waiting time

from queues import Queue
from printer import Printer, Task
import random

# TODO Implement ability to reflect effect of more students, shorter average length of print task
def simulation(n_seconds: int, ppm: int) -> None:
    # Initialize printer, queue and waiting times list
    lab_printer = Printer(ppm)
    print_queue = Queue()
    wait_times = []

    # Iterate through every second of simulation
    for current_second in range(n_seconds):
        if new_print_task():
            # If there is a new task, add it to the queue
            task = Task(current_second)
            print_queue.enqueue(task)

        # If the printer is not busy, and there is a new task pending
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            # Start the task, and add waiting time to list
            next_task = print_queue.dequeue()
            wait_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()  # Decrement timer or set to idle

    # Calculate and print average waiting times and tasks left
    avg_wait = sum(wait_times) / len(wait_times)
    print(
        "Average wait %6.2f secs %3d tasks remaining." % (avg_wait, print_queue.size())
    )


def new_print_task() -> bool:
    num = random.randrange(1, 181)  # Chance that task appear
    if num == 180:  # Only create task if num is 180
        return True
    return False


# 10 rounds with 3600 seconds and 5 ppm printer
for i in range(10):
    simulation(3600, 5)

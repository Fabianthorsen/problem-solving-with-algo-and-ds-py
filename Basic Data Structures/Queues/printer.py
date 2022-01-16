from __future__ import annotations


class Printer:
    def __init__(self, ppm: int):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    # Decrement time or set printer to idle
    def tick(self) -> None:
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining < 0:
                self.current_task = None

    # Keep track if printer is busy or not
    def busy(self) -> bool:
        if self.current_task != None:
            return True
        else:
            return False

    # Start next task from queue
    def start_next(self, task: Task) -> None:
        self.current_task = task
        self.time_remaining = task.get_pages() * 60 / self.page_rate


import random


class Task:
    def __init__(self, time: int):
        self.timestamp = time
        self.pages = random.randrange(1, 21)  # Random integer between 1 to 20 inclusive

    # Getter for timestamp
    def get_stamp(self) -> int:
        return self.timestamp

    # Getter for pages
    def get_pages(self) -> int:
        return self.pages

    # Getter for current waiting time
    def wait_time(self, current_time: int) -> int:
        return current_time - self.timestamp

import datetime
import os
from typing import *

class InvalidInputError(Exception):
    """Exception which happens when the user provides Invalid Input"""

class Task:
    def __init__(self, name: str, duration: int):
        self.name = name
        self.duration = duration

def _split(task: Task, time: int) -> Tuple[Task, Task]:
    if task.duration < time:
        raise InvalidInputError(f"Cannot split task {task.name} with duration {task.duration} minuts at the {time} minute mark.")

    otask = Task(task.name, task.duration - time)
    task.duration = time
    return (task, otask)

class TaskList:
    def __init__(self, start_time = datetime.datetime(1, 1, 1, 7, 0)):
        self._internal_list = []
        self.start_time = start_time

    # ---------------

    # BEGIN append
    def _append(self, task: Task):
        self._internal_list.append(task)
    

    def append(self, name: str, duration: int):
        self._append(Task(name, duration))
    # END append

    # ---------------
    
    # BEGIN insert
    def _insert(self, task: Task, idx: int = 0):
        self._internal_list.insert(idx, task)
    

    def insert(self, name: str, duration: int, idx: int = 0):
        self._insert(Task(name, duration), idx)
    # END insert

    # ---------------

    # BEGIN insert_splice
    def _insert_splice(self, task: Task, time: int, idx: int = 0):
        t1, t2 = _split(self._internal_list[idx], time)
        self._internal_list[idx] = t1
        self._internal_list.insert(idx+1, task)
        self._internal_list.insert(idx+2, t2)


    def insert_splice(self, name: str, duration: int, time: int, idx: int = 0):
        self._insert_splice(Task(name, duration), time, idx=idx)
    # END insert_splice

    def __len__(self):
        return len(self._internal_list)
    
    def __getitem__(self, idx):
        return self._internal_list[idx]

    def __str__(self):
        ct = self.start_time

        out_str = ""
        out_str += "_____________________________\n"
        for task in self._internal_list:
            td = datetime.timedelta(minutes = task.duration)
            out_str += f"{task.name} | {ct.strftime('%H:%M')} | {(td+ct).strftime('%H:%M')}\n"
            ct += td
        out_str+="‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"

        return out_str

def main():
    tl = TaskList()
    tl.append("Task 1", 60)
    print(str(tl))
    input()
    tl.insert("Task 2", 60, 0)
    print(str(tl))
    input()
    tl.insert_splice("Task 3", 60, 1)
    print(str(tl))
    input()
if __name__ == "__main__":
    main()
import sched
import time
from typing import Callable


class Scheduler(object):

    PRIORITY_HIGH = 0
    PRIORITY_MEDIUM = 1
    PRIORITY_LOW = 2

    def __init__(self):
        self.__scheduler = sched.scheduler(time.time)

    def now(self, action: Callable, priority:int=PRIORITY_HIGH, argument=(), kwargs={}):
        """Method that executes the action in 15 seconds 

        Args:
            action (Callable): task to be performed 
            priority (int, optional): Priority level of execution. Defaults to PRIORITY_HIGH.
            argument (tuple, optional): arguments from action callable. Defaults to ().
            kwargs (dict, optional): key arguments from action callable. Defaults to {}.
        """
        self.__scheduler.enter(15, priority, action,
                               argument=argument, kwargs={})

    def run(self):
        self.__scheduler.run(blocking=True)

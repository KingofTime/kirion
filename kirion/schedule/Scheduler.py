from datetime import datetime, timedelta
import sched
import time
from typing import Callable


class Scheduler(object):

    PRIORITY_HIGH = 0
    PRIORITY_MEDIUM = 1
    PRIORITY_LOW = 2
    DATE_FORMAT = '%d/%m/%Y'
    TIME_FORMAT = '%H:%M'

    def __init__(self):
        self.__date = None
        self.__time = None
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

    def specific_horary(self, action, priority=PRIORITY_HIGH, argument=(), kwargs={}):
        """Method that executes the action in specific horary using the attributes date/time

        Args:
            action (Callable): task to be performed 
            priority (int, optional): Priority level of execution. Defaults to PRIORITY_HIGH.
            argument (tuple, optional): arguments from action callable. Defaults to ().
            kwargs (dict, optional): key arguments from action callable. Defaults to {}.
        """

        horary = datetime.combine(self.__date, self.__time)
        self.__scheduler.enterabs(horary.timestamp(), priority, action, argument=argument, kwargs=kwargs)
    
    def every_day(self, action, priority=PRIORITY_HIGH, argument=(), kwargs={}):
        """Method that executes the action every day in the specific time

        Args:
            action (Callable): task to be performed 
            priority (int, optional): Priority level of execution. Defaults to PRIORITY_HIGH.
            argument (tuple, optional): arguments from action callable. Defaults to ().
            kwargs (dict, optional): key arguments from action callable. Defaults to {}.
        """

        def reschedule(horary, *argument, **kwargs):
            horary += timedelta(days=1)
            print(f"{horary}")
            action(*argument, **kwargs)

            self.__scheduler.enterabs(horary.timestamp(), priority, reschedule, argument=argument, kwargs=kwargs)

        
        horary = datetime.combine(datetime.now(), self.__time)
        if horary.timestamp() < datetime.now().timestamp():
                horary += timedelta(days=1)
        
        argument =  horary, *argument
        print(f"{horary}")

        self.__scheduler.enterabs(horary.timestamp(), priority, reschedule, argument=argument, kwargs=kwargs)

    def run(self):
        self.__scheduler.run(blocking=True)
    
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = datetime.strptime(value, self.DATE_FORMAT)

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = datetime.strptime(value, self.TIME_FORMAT).time()




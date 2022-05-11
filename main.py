from kirion.schedule import Scheduler


scheduler = Scheduler()


def task():
    print("Tarefa bonita")

scheduler.time = '00:36'

scheduler.every_day(task)


scheduler.run()

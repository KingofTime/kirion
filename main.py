from kirion.schedule import Scheduler


scheduler = Scheduler()


def task():
    print("Tarefa bonita")


scheduler.now(task)


scheduler.run()

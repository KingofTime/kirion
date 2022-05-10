from kirion.schedule import Scheduler


scheduler = Scheduler()


def task():
    print("Tarefa bonita")


scheduler.date = '10/05/2022'
scheduler.time = '10:21'

scheduler.specific_date(task)


scheduler.run()

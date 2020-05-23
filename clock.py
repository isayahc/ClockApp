from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()
'''
Implementation for TXTA:
use sheduled_job to start time_job at marekt open
Use sheduled_job to end time_job at market close

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('start algorithm.')
    @sched.scheduled_job('interval', minutes=3)
    def timed_job(n):
        print('This job is run every n minutes.')

    @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
    def scheduled_job():
        scheduler.shutdown()


'''
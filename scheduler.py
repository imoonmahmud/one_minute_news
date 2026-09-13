from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from main import run

sched = BlockingScheduler()
sched.add_job(run, CronTrigger(hour="9,12,15,18,21", minute=0))

if __name__ == "__main__":
    print("News bot scheduler started. Running every 3 hours...")
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")
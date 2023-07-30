from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import daily_login_bonus

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(daily_login_bonus, 'interval', hours=24)
    scheduler.start()
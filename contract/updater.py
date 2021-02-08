from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from contract import views

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(views.call_screen_msg, 'interval', minutes=1)
    scheduler.start()

def start1():
    scheduler = BackgroundScheduler()
    scheduler.add_job(views.call_betterplace_schedular_fun, 'cron', day_of_week='mon-sun', hour=22, minute=30)
    scheduler.start()

    

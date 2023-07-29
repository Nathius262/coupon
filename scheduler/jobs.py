from pipay.models import DailyLoginTask

def daily_login_bonus():
    print("daily")
    reset_all_user_daily_task = DailyLoginTask.objects.all()
    reset_all_user_daily_task.update(task_completed=False)
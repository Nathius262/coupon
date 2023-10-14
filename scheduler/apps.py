from django.apps import AppConfig

class SchedulerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "scheduler"
    
    def ready(self):
        from scheduler import scheduler
        scheduler.start()
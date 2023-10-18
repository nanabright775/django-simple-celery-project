from django.shortcuts import render
from django_celery_beat.models import CrontabSchedule,PeriodicTask,ClockedSchedule
from datetime import datetime,timedelta

def home(request):
    
    current_time = datetime.now()
    # print(current_time, ',,,')   
    new_time = current_time + timedelta(minutes=2)

    
    schedule = ClockedSchedule()
    
    PeriodicTask.objects.create(crontab = schedule ,name='task9', task = 'mainapp.tasks.add_first')
    
    
    return render(request, 'home.html')
from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)
from .models import Counter 
 
@shared_task(bind=True)
def add_first(self):
    counter = Counter.objects.first()
    counter.number = counter.number + 20
    counter.save()
    logger.info(str(counter.number)) 
    # logger.info("first task celery bright")
    return 'done'
from task.celery_blog import func
from task.celery_add import add

func(['https://google.com', 'https://facebook.com'])
add.delay(4, 5)

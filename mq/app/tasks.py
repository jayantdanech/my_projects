from celery import Celery
import time

app = Celery(
    'tasks',
    broker='amqp://guest:guest@rabbitmq:5672//',
    backend='redis://redis:6379/0'   # <-- Added this line
)

@app.task
def process_data(x, y):
    time.sleep(3)
    return x + y


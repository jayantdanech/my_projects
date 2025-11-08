from celery import Celery
import time

# Connect Celery to RabbitMQ broker
#app = Celery('tasks', broker='amqp://guest@rabbitmq//')
app = Celery('tasks', broker='amqp://guest:guest@rabbitmq:5672//')

@app.task
def process_data(x, y):
    time.sleep(3)  # Simulate heavy work
    return x + y


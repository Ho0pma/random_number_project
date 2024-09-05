from celery import shared_task
from random import randint
from .redis_client import redis_client


@shared_task
def update_random_number():
    number = randint(0, 10)
    redis_client.set('random_number', number)
    return number

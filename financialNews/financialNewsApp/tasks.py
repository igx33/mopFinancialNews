from celery import shared_task
from financialNewsApp import work


@shared_task(name='fetch_news')
def fetch_news():
    """
    Run work.get_news() task

    :return: none
    """
    work.get_news()

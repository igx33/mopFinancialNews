from django.test import TransactionTestCase
from financialNewsApp.models import Symbol, News
from financialNewsApp.work import get_news, create_news_object
from unittest.mock import patch


class Entry:
    """
    This class only serves for mocking parsed rss response
    """
    def __init__(self, title, description, guid, link, published):
        self.title = title
        self.description = description
        self.guid = guid
        self.link = link
        self.published = published


# Fake (mocked) parse response data
response = {
    'entries': [
        Entry(title='TestTitle', description='TestDescription', guid='TestGUID', link='TestLink',
              published='TestPublishedDate'),
        Entry(title='TestTitle2', description='TestDescription2', guid='TestGUID2', link='TestLink2',
              published='TestPublishedDate2'),
    ],
}


class WorkCreateNewObjectTestCase(TransactionTestCase):
    def setUp(self):
        Symbol.objects.create(short_name="TEST", full_name="Test")

    def test_create_news_object(self):
        symbol = Symbol.objects.get(short_name='TEST')
        self.assertEqual(symbol.full_name, 'Test')

        news = create_news_object(response['entries'][0], symbol, News)
        self.assertEqual(news.title, 'TestTitle')

    @patch("feedparser.parse", return_value=response)
    def test_get_news(self, mocked):
        get_news()
        news = News.objects.get(title='TestTitle')

        self.assertEqual(news.title, 'TestTitle')
        self.assertEqual(news.description, 'TestDescription')
        self.assertEqual(news.pub_date, 'TestPublishedDate')
        self.assertEqual(news.symbol.full_name, 'Test')






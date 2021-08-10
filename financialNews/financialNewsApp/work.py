import feedparser
from django.db import IntegrityError
from django.utils import timezone

YAHOO_FINANCE_RSS_API_BASE = 'https://feeds.finance.yahoo.com/rss/2.0/'
YAHOO_FINANCE_QUERY_P1 = 'headline?s='
YAHOO_FINANCE_QUERY_P2 = '&region=US&lang=en-US'


def get_parsed_document(symbol):
    """
    Fetches and parses RSS Feed.

    :param symbol:
    :return: {entries:[{title, description, guid, link, published, link}]}
    """
    return feedparser.parse(
        YAHOO_FINANCE_RSS_API_BASE + YAHOO_FINANCE_QUERY_P1 + symbol.short_name + YAHOO_FINANCE_QUERY_P2)


def create_news_object(entry, symbol, news_model):
    """
    Creates new News object, without storing it in the DB

    :param entry:
    :param symbol:
    :param news_model:
    :return: A :class: `News`
    """
    return news_model(symbol=symbol,
                      description=entry.description,
                      original_guid=entry.guid,
                      link=entry.link,
                      pub_date=entry.published,
                      title=entry.title,
                      created_date=timezone.now()
                      )


def get_news():
    """
    Fetch financial news from Yahoo Rss, parse and store in the DB

    :return: none
    """
    # TODO: This import should be moved up. It's here for now because Celery complains about app loading
    from financialNewsApp.models import Symbol, News
    all_symbols = Symbol.objects.all()

    for symbol in all_symbols:
        document = get_parsed_document(symbol)
        for entry in document['entries']:
            try:
                news = create_news_object(entry, symbol, News)
                news.save()

            except IntegrityError:
                pass  # already exists, so,  don't create

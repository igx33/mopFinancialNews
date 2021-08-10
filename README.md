# MOP Financial News System

## Original Task:

Description:

Create Django based REST api service for financial news. Service will have two parts: REST api service and scraping service.
REST api will be primarily used  for fetching data and scraping service will collect and store data from Yahoo finance site. 

Scraper service will use Yahoo RSS feed for collecting data (https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US, getting data for AAPL symbol Apple Inc).

Scraper service scheduler can be implemented with celery extension https://github.com/celery/django-celery-beat


## Original Requirements

Use Django rest framework to implement REST api service. [Y]

News will be fetched per symbol. [Y]

Implement pagination. [Y]

Use Celery for async tasks and periodic scraping. [Y]

Use Postgresql as DB solution. [Y]

Collect news for following symbols, AAPL, TWTR, GC=F(GOLD), INTC. [Y]

Dockreize project (services will be run in Docker containers). [Y]

Write unit tests for most important code parts. [Y]

Submit project to Github. [Y]


--------------------------------------------------------------------

## Running:

```bash
docker-compose up --build -d
```

This command will start the following:
* Postgres DB
* Redis
* Django Web App
* Celery worker service
* Celery beat service

While starting the app, docker will automatically run the following:
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py test --noinput`
* `python manage.py generateschema --file openapi-schema.yml`

There is no need to manually insert the starting data as it will be seeded in the DB during the migration process.


## Accessing the API:

Address: `http://localhost:1337/api/news/`

Options:
* Query by (`example: ...?title=First News&symbol__short_name=AAPL`):
  * id, 
  * symbol__short_name, 
  * title, 
  * description, 
  * pub_date
* Search by (`example: ...?search=Apple to invest`):
  * title,
  * description,
  * pub_date
* Pagination (`example: ...?page=2`):

Additional features:
* Basic cashing (10 min)
* Request Throttling (1k requests per user per day)

## Basic tests:

The most basic form of unit tests that demonstrate mocking and running can be found in:
`financialNews\financialNewsApp\tests.py`

Will populate and clear the test sqlite3 DB each time they are executed.

from django.db import models


class Symbol(models.Model):
    short_name = models.CharField(max_length=10,)
    full_name = models.CharField(max_length=100,)

    def __str__(self):
        return self.full_name


class News(models.Model):
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    description = models.CharField(max_length=10000)
    original_guid = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=1000)
    pub_date = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    created_date = models.DateTimeField('date created')

    def __str__(self):
        return self.title

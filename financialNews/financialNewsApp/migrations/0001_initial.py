# Generated by Django 3.2.4 on 2021-08-07 17:31

from django.db import migrations, models
import django.db.models.deletion

# Initial Symbols seed
def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Symbol = apps.get_model("financialNewsApp", "Symbol")
    db_alias = schema_editor.connection.alias
    Symbol.objects.using(db_alias).bulk_create([
        Symbol(short_name="AAPL", full_name="Apple"),
        Symbol(short_name="TWTR", full_name="Twitter"),
        Symbol(short_name="GC=F", full_name="Gold"),
        Symbol(short_name="INTC", full_name="Intel"),
    ])

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=10)),
                ('full_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10000)),
                ('original_guid', models.CharField(max_length=100, unique=True)),
                ('link', models.CharField(max_length=1000)),
                ('pub_date', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=1000)),
                ('created_date', models.DateTimeField(verbose_name='date created')),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financialNewsApp.symbol')),
            ],
        ),
        migrations.RunPython(forwards_func),
    ]

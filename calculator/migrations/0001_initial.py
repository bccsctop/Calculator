# Generated by Django 3.0.2 on 2020-02-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input1', models.FloatField(blank=True)),
                ('input2', models.FloatField(blank=True)),
                ('result', models.FloatField(blank=True)),
            ],
        ),
    ]
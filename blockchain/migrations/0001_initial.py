# Generated by Django 2.2.5 on 2020-05-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TheBlockchain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockchain', models.CharField(max_length=100000000)),
            ],
        ),
    ]

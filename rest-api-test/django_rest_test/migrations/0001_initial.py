# Generated by Django 2.1 on 2018-09-26 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=2948)),
            ],
        ),
    ]
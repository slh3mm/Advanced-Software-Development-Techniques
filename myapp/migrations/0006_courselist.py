# Generated by Django 4.1.7 on 2023-04-25 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_merge_20230416_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
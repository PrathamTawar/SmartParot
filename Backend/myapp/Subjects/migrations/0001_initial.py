# Generated by Django 5.1.4 on 2024-12-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectName', models.CharField(max_length=100)),
                ('SubjectDesc', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 3.2.10 on 2021-12-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=100)),
                ('name', models.CharField(max_length=30)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user_id', models.IntegerField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('DONE', 'Done')], default='PENDING', max_length=10)),
            ],
        ),
    ]

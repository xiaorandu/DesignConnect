# Generated by Django 3.2 on 2023-03-24 14:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(help_text='Who post this tweet', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user', '-created_at'),
                'index_together': {('user', 'created_at')},
            },
        ),
        migrations.CreateModel(
            name='TweetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('order', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default=0)),
                ('has_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tweet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tweets.tweet')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'index_together': {('status', 'created_at'), ('user', 'created_at'), ('tweet', 'order'), ('has_deleted', 'created_at')},
            },
        ),
    ]

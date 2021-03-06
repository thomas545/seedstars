# Generated by Django 3.0.4 on 2020-03-19 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.CharField(blank=True, max_length=250, null=True)),
                ('python_tip', models.TextField(blank=True, null=True)),
                ('who_posted', models.CharField(blank=True, max_length=200, null=True)),
                ('published', models.BooleanField(default=False)),
                ('retweet_count', models.IntegerField(default=0)),
                ('favorite_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('expanded_url', models.CharField(blank=True, max_length=200, null=True)),
                ('display_url', models.CharField(blank=True, max_length=200, null=True)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to='tweets.Tweet')),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-17 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0003_remove_newslettersubscriber_last_sent_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newslettersubscriber",
            name="subscription_date",
        ),
    ]

# Generated by Django 5.2.4 on 2025-07-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_blog', '0003_articletag_articlepage_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]

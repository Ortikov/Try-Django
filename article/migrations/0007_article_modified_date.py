# Generated by Django 4.2.7 on 2023-11-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_created_date_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

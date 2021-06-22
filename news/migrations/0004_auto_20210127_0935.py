# Generated by Django 3.1.5 on 2021-01-27 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210126_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='preview',
            field=models.TextField(unique=True, verbose_name='PREVIEW'),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(help_text='news title', max_length=300, verbose_name='TITLE'),
        ),
    ]
# Generated by Django 2.2.2 on 2019-06-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default='01/01/1900'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]

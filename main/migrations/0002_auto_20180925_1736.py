# Generated by Django 2.1 on 2018-09-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='language',
        ),
        migrations.AddField(
            model_name='participant',
            name='language1',
            field=models.CharField(blank=True, choices=[('Filipino', 'Filipino'), ('English', 'English'), ('Hokkien', 'Hokkien'), ('Mandarin', 'Mandarin'), ('Korean', 'Korean'), ('Japanese', 'Japanese'), ('Bisaya/Cebuano', 'Bisaya/Cebuano')], default='not specified', max_length=200, null=True, verbose_name='language1'),
        ),
        migrations.AddField(
            model_name='participant',
            name='language2',
            field=models.CharField(blank=True, choices=[('Filipino', 'Filipino'), ('English', 'English'), ('Hokkien', 'Hokkien'), ('Mandarin', 'Mandarin'), ('Korean', 'Korean'), ('Japanese', 'Japanese'), ('Bisaya/Cebuano', 'Bisaya/Cebuano')], default='not specified', max_length=200, null=True, verbose_name='language2'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='idnumber',
            field=models.CharField(default='not specified', max_length=8),
        ),
        migrations.AlterField(
            model_name='participant',
            name='mobile',
            field=models.CharField(default='not specified', max_length=11),
        ),
    ]
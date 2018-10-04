# Generated by Django 2.1 on 2018-09-25 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnumber', models.CharField(default='not specified', max_length=200)),
                ('first_name', models.CharField(default='not specified', max_length=200)),
                ('last_name', models.CharField(default='not specified', max_length=200)),
                ('mobile', models.CharField(default='not specified', max_length=200)),
                ('email', models.EmailField(default='not specified', max_length=200)),
                ('birthday', models.DateField(default='not specified', max_length=200)),
                ('college', models.CharField(choices=[('BAGCED', 'BAGCED'), ('CCS', 'CCS'), ('COL', 'COL'), ('CLA', 'CLA'), ('COS', 'COS'), ('GCOE', 'GCOE'), ('RVRCOB', 'RVRCOB'), ('SOE', 'SOE')], default='not specified', max_length=200, verbose_name='college')),
                ('degree', models.CharField(default='not specified', max_length=200)),
                ('language', models.CharField(blank=True, choices=[('Filipino', 'Filipino'), ('English', 'English'), ('Hokkien', 'Hokkien'), ('Mandarin', 'Mandarin'), ('Korean', 'Korean'), ('Japanese', 'Japanese'), ('Bisaya/Cebuano', 'Bisaya/Cebuano')], default='not specified', max_length=200, null=True, verbose_name='language')),
                ('question1', models.CharField(blank=True, default='not specified', max_length=200, null=True)),
                ('question2', models.CharField(blank=True, default='not specified', max_length=200, null=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='date_counted')),
            ],
        ),
    ]
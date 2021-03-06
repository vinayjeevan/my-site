# Generated by Django 3.0.6 on 2020-07-08 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_name', models.CharField(max_length=50, null=True)),
                ('com_location', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Agent_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50, null=True)),
                ('call_atd', models.IntegerField()),
                ('time_dur', models.TimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_site.Company_name')),
            ],
        ),
    ]

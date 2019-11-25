# Generated by Django 2.2.7 on 2019-11-25 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_initial_data_20191125_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='sys_company',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='system.Company'),
        ),
        migrations.AlterField(
            model_name='accounttype',
            name='id',
            field=models.CharField(editable=False, max_length=15, primary_key=True, serialize=False),
        ),
    ]
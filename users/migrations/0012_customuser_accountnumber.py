# Generated by Django 2.2.6 on 2019-11-12 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_customuser_accountnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='accountNumber',
            field=models.CharField(default='12', max_length=16),
        ),
    ]
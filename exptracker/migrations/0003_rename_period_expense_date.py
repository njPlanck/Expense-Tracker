# Generated by Django 4.1.5 on 2023-04-30 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exptracker', '0002_remove_expense_date_expense_period'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='period',
            new_name='date',
        ),
    ]
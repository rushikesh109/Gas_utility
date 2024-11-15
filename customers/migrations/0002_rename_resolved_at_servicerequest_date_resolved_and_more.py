# Generated by Django 5.1.3 on 2024-11-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerequest',
            old_name='resolved_at',
            new_name='date_resolved',
        ),
        migrations.RenameField(
            model_name='servicerequest',
            old_name='created_at',
            new_name='date_submitted',
        ),
        migrations.RenameField(
            model_name='servicerequest',
            old_name='description',
            new_name='details',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='customer',
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='request_type',
            field=models.CharField(choices=[('installation', 'Installation'), ('maintenance', 'Maintenance'), ('repair', 'Repair')], max_length=20),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')], default='pending', max_length=20),
        ),
    ]

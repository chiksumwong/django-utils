# Generated by Django 3.0.6 on 2020-05-13 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_schedule_job', '0002_auto_20200511_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='synctask',
            name='action',
            field=models.SmallIntegerField(choices=[(2, 'get'), (3, 'update'), (0, 'list'), (1, 'create')]),
        ),
        migrations.AlterField(
            model_name='synctask',
            name='category',
            field=models.SmallIntegerField(choices=[(1, 'product'), (0, 'application')]),
        ),
        migrations.AlterField(
            model_name='synctask',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'pending'), (2, 'sent'), (0, 'archive')], default=1),
        ),
    ]
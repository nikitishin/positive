# Generated by Django 2.2.6 on 2019-11-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vbot', '0002_viberuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='viberuser',
            name='viber_id',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='country',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='device_type',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='is_blocked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='language',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='primary_device_os',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]

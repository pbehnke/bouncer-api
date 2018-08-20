# Generated by Django 2.1 on 2018-08-20 09:40

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20180820_0923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authtoken',
            options={},
        ),
        migrations.AlterField(
            model_name='authtoken',
            name='key',
            field=models.CharField(default=authentication.models.AuthToken.generate_key, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
    ]

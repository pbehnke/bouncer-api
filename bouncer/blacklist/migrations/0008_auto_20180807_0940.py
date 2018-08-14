# Generated by Django 2.1 on 2018-08-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("blacklist", "0007_emailentry_hashed_value")]

    operations = [
        migrations.AlterField(
            model_name="emailentry",
            name="lower_case_entry_value",
            field=models.EmailField(editable=False, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="emailhostentry",
            name="lower_case_entry_value",
            field=models.CharField(editable=False, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="ipentry",
            name="lower_case_entry_value",
            field=models.GenericIPAddressField(editable=False, unique=True),
        ),
    ]

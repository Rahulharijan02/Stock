# Generated by Django 4.1 on 2022-10-16 05:45

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_stock"),
    ]

    operations = [
        migrations.AddField(
            model_name="stock",
            name="dslug",
            field=autoslug.fields.AutoSlugField(
                editable=False, null=True, populate_from="description", unique=True
            ),
        ),
    ]

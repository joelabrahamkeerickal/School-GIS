# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_auto_20180207_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolinfo',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-25 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0010_alter_label_is_share'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='is_share',
            field=models.BooleanField(choices=[(0, True), (1, False)], default=1),
        ),
    ]

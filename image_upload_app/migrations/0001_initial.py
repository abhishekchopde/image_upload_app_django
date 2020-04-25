# Generated by Django 2.0.2 on 2020-04-16 13:48

from django.db import migrations, models
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageHash', models.CharField(default='default', max_length=32)),
                ('imageType', models.CharField(default='jpg', max_length=15)),
                ('uploadedBy', jsonfield.fields.JSONField()),
                ('uploadedAt', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'db_table': 'images',
            },
        ),
    ]
# Generated by Django 3.0.8 on 2020-08-15 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_auto_20200815_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='packages.Package'),
        ),
    ]

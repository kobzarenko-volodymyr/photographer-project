# Generated by Django 2.1.7 on 2019-04-10 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20190410_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumimage',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Album'),
        ),
    ]

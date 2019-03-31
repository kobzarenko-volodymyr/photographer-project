# Generated by Django 2.1.7 on 2019-03-31 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='albums')),
                ('thumb', models.ImageField(upload_to='albums')),
                ('alt', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='thumb',
            field=models.ImageField(upload_to='albums'),
        ),
        migrations.AddField(
            model_name='albumimage',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gallery.Album'),
        ),
    ]

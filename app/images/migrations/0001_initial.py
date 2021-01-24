# Generated by Django 3.1.2 on 2020-10-28 09:34

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.ImageField(blank=True, null=True, upload_to=images.models.user_directory_path)),
            ],
        ),
    ]
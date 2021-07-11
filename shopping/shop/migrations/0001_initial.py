# Generated by Django 3.1.3 on 2021-06-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Closet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=10, unique=True)),
                ('clothes_name', models.CharField(max_length=20, unique=True, verbose_name='이름')),
                ('clothes_category', models.CharField(blank=True, choices=[('상의', 'top'), ('반팔', 'short_shirt'), ('긴팔', 'long_shirt'), ('민소매', 'sleeveless_shirt'), ('하의', 'bottom'), ('바지', 'pants'), ('치마', 'skirt'), ('원피스', 'dress')], max_length=10)),
                ('clothes_color', models.CharField(blank=True, choices=[('Red', 'Red'), ('Pink', 'Pink'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue'), ('Purple', 'Purple'), ('Black', 'Black'), ('Grey', 'Grey')], max_length=10)),
                ('clothes_image', models.ImageField(upload_to='')),
                ('put_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
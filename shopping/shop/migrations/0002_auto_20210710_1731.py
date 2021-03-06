# Generated by Django 3.1.3 on 2021-07-10 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='closet',
            name='use_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='closet',
            name='clothes_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='옷 이름'),
        ),
        migrations.AlterField(
            model_name='closet',
            name='user_id',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.category')),
            ],
            options={
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.AlterField(
            model_name='closet',
            name='clothes_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
    ]

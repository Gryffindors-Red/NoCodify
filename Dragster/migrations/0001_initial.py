# Generated by Django 4.2 on 2023-05-04 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='UnTitled', max_length=200)),
                ('description', models.CharField(default='Author not provied any description', max_length=200)),
                ('content', models.CharField(default='Author not provied any description', max_length=2000)),
                ('blog_profile_img', models.CharField(default='https://www.equalityhumanrights.com/sites/default/files/styles/listing_image/public/default_images/blog-teaser-default-full_5.jpg?itok=YOsTg-7X', max_length=2000)),
                ('categories', models.CharField(max_length=200)),
                ('updated_date', models.DateField(default=django.utils.timezone.now)),
                ('Block_chin_blockNo', models.CharField(max_length=50)),
                ('trans_detial', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(max_length=255)),
                ('response', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('html', models.TextField()),
                ('css', models.TextField()),
                ('preview_link', models.TextField()),
                ('Block_chin_blockNo', models.CharField(max_length=50)),
                ('trans_detial', models.CharField(max_length=50)),
                ('ipfs', models.CharField(max_length=100)),
            ],
        ),
    ]
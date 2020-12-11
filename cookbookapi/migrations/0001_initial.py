# Generated by Django 3.1.4 on 2020-12-10 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CbUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=250)),
                ('picture', models.ImageField(null=True, upload_to='recipe_image_url')),
                ('ingredients', models.CharField(max_length=300)),
                ('directions', models.CharField(max_length=950)),
                ('notes', models.CharField(max_length=350)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbookapi.cbuser')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbookapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbookapi.cbuser')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbookapi.recipe')),
            ],
        ),
    ]
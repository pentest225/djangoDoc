# Generated by Django 2.2.8 on 2020-02-09 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='Categorie/%Y/%m/%d/')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='article/')),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_upd', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie_article', to='myApp.Categorie')),
                ('tag', models.ManyToManyField(related_name='tag_article', to='myApp.Tag')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]

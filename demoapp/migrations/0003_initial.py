# Generated by Django 5.1 on 2024-09-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('demoapp', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('pnmae', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]

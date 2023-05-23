# Generated by Django 4.2.1 on 2023-05-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_time_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='user_contact_name')),
                ('surname', models.CharField(max_length=100, verbose_name='surname_contact_name')),
                ('email', models.CharField(max_length=100, verbose_name='user_email')),
                ('feedback', models.CharField(max_length=100, verbose_name='user_feedback')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category_name', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['time_create', 'name'], 'verbose_name': 'product_name', 'verbose_name_plural': 'products'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='time_create',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='time_create',
            field=models.DateField(auto_now_add=True, verbose_name='creation_date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='time_update',
            field=models.DateField(auto_now=True, verbose_name='update_date'),
        ),
    ]

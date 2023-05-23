# Generated by Django 4.2.1 on 2023-05-23 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
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
    ]
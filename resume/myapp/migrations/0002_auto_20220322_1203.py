# Generated by Django 3.1 on 2022-03-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='state',
            field=models.CharField(choices=[('Dhaka', 'Dhaka'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Cumilla', 'Cumilla'), ('Barisal', 'Barisal'), ('Myminsingh', 'Myminsingh'), ('chattrogram', 'chattrogram'), ('Rangpur', 'Rangpur')], max_length=50),
        ),
    ]

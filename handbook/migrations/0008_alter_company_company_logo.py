# Generated by Django 4.0 on 2021-12-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0007_alter_company_comapny_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
    ]
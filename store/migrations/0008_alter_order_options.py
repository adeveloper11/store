# Generated by Django 4.2.3 on 2023-08-28 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_customer_options_remove_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancle_order', 'Can cancle order')]},
        ),
    ]
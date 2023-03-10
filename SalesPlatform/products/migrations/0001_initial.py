# Generated by Django 4.0.5 on 2022-06-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company_name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('1', 'Men wear'), ('2', 'Women wear'), ('3', 'Bags'), ('4', 'Watches'), ('5', 'Kids')], max_length=128)),
            ],
        ),
    ]

# Generated by Django 2.1.1 on 2019-01-06 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_menu_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='amount',
        ),
        migrations.AddField(
            model_name='beverages',
            name='beverages_amt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='breads',
            name='breads_amt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='desserts',
            name='desserts_amt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='rice',
            name='rice_amt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='sabzi',
            name='sabzi_amt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='snacks',
            name='snacks_amt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='streetfood',
            name='streetfood_amt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='thali',
            name='thali_amt',
            field=models.FloatField(default=0),
        ),
    ]

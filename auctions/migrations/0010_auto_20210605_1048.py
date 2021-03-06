# Generated by Django 3.2.3 on 2021-06-05 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20210531_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='winner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='auctions.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='winner',
            name='listingid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_winner', to='auctions.listings'),
        ),
    ]

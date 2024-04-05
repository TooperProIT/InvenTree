# Generated by Django 3.2.19 on 2023-06-06 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0101_stockitemtestresult_metadata'),
        ('build', '0046_auto_20230606_1033'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='builditem',
            unique_together={('build_line', 'stock_item', 'install_into')},
        ),
        migrations.RemoveField(
            model_name='builditem',
            name='bom_item',
        ),
        migrations.RemoveField(
            model_name='builditem',
            name='build',
        ),
    ]
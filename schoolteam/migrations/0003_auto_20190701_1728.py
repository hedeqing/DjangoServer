# Generated by Django 2.2.2 on 2019-07-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolteam', '0002_auto_20190701_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendcontest',
            name='category',
            field=models.CharField(choices=[('Sophomore', '大二'), ('Freshman', '大一'), ('Junior', '大三'), ('Senior', '大四')], max_length=128),
        ),
        migrations.AlterField(
            model_name='team',
            name='category',
            field=models.CharField(choices=[('traval', '出行'), ('study', '学习'), ('game', '游戏'), ('contest', '比赛')], max_length=128),
        ),
    ]

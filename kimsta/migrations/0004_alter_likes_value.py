# Generated by Django 3.2.7 on 2021-12-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kimsta', '0003_alter_likes_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Dislike', 'Dislike')], default='like', max_length=10),
        ),
    ]

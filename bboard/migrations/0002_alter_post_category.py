# Generated by Django 4.2.8 on 2023-12-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Танки', 'Танки'), ('Хилеры', 'Хилы'), ('ДД', 'ДД'), ('Торговцы', 'Торговцы'), ('Гилдмастеры', 'Гилдмастеры'), ('Квестгиверы', 'Квестгиверы'), ('Кузнецы', 'Кузнецы'), ('Кожевенники', 'Кожевники'), ('Зельевары', 'Зельевары'), ('Мастера заклинаний', 'Мастера заклинаний')], default='tanks', max_length=255, verbose_name='Категория'),
        ),
    ]

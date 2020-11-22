# Generated by Django 3.1.2 on 2020-11-21 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20201107_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdrivemodel',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='autoch', to='main_app.autocharacters', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='autocharacters',
            name='is_favorite',
            field=models.BooleanField(blank=True, default=False, verbose_name='В "Избранных"'),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=80, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=11, verbose_name='Номер телефона'),
        ),
    ]
# Generated by Django 3.0 on 2019-12-16 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='autor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.Pessoa'),
        ),
    ]

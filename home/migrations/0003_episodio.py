# Generated by Django 4.0.4 on 2022-06-24 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_descicao_curso_descricao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('video', models.URLField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodios', to='home.curso')),
            ],
        ),
    ]

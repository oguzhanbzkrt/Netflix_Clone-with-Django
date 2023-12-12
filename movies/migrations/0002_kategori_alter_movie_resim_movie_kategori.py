# Generated by Django 4.2.8 on 2023-12-06 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='resim',
            field=models.FileField(blank=True, null=True, upload_to='filmler/', verbose_name='Film Resmi'),
        ),
        migrations.AddField(
            model_name='movie',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.kategori'),
        ),
    ]

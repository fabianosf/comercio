# Generated by Django 4.0.6 on 2022-07-27 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome do Produto')),
                ('descricao', models.TextField(verbose_name='Descrição do Produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço do Produto')),
                ('imagem', models.ImageField(upload_to='')),
                ('status', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='categoria.categoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]

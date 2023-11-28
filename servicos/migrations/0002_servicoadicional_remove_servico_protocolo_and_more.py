# Generated by Django 4.2.7 on 2023-11-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicoAdicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('preco', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='servico',
            name='protocolo',
        ),
        migrations.AddField(
            model_name='servico',
            name='identificador',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='servico',
            name='protocole',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
        migrations.AlterField(
            model_name='categoriamanutencao',
            name='titulo',
            field=models.CharField(choices=[('TVM', 'Trocar válcula do motor'), ('TO', 'Troca de óleo'), ('B', 'Balanceamento')], max_length=3),
        ),
        migrations.AddField(
            model_name='servico',
            name='servicos_adicionais',
            field=models.ManyToManyField(to='servicos.servicoadicional'),
        ),
    ]

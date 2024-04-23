# Generated by Django 4.0.3 on 2023-09-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=50)),
                ('banco', models.CharField(choices=[('NU', 'Nubank'), ('CX', 'Caixa Econômica'), ('BCO', 'Bradesco'), ('IN', 'Inter')], max_length=3)),
                ('tipo', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2)),
                ('valor', models.FloatField()),
                ('icone', models.ImageField(upload_to='icones')),
            ],
        ),
    ]

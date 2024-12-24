# Generated by Django 5.1.4 on 2024-12-24 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('telephone', models.CharField(max_length=15)),
                ('classe_choix', models.CharField(choices=[('L1', 'Licence 1'), ('L2', 'Licence 2'), ('L3', 'Licence 3'), ('M1', 'Master 1'), ('M2', 'Master 2')], max_length=10)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

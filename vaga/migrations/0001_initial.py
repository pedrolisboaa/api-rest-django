# Generated by Django 5.0 on 2023-12-20 19:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("habilidade", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vaga",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=256)),
                ("descricao", models.TextField()),
                ("empresa", models.CharField(max_length=256)),
                ("local", models.CharField(max_length=256)),
                (
                    "salario",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                ("ativa", models.BooleanField(default=True)),
                ("habilidades", models.ManyToManyField(to="habilidade.habilidade")),
            ],
        ),
    ]

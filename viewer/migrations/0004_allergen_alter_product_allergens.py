# Generated by Django 4.1.1 on 2024-09-22 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_rename_category_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='allergens',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.allergen'),
        ),
    ]

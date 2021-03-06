# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(help_text='Enter an ingredient name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_type_description', models.CharField(help_text='Enter a description of ingredient type', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(help_text='Enter a recipe title', max_length=200)),
                ('recipe_description', models.CharField(help_text='enter a breif description of the recipe', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeSteps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.IntegerField()),
                ('instructions', models.CharField(help_text='Enter a instruction for recipe step', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeStepsIngredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_required', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.2.11 on 2024-03-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nutrients", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foodnutrientfact",
            name="calorie",
            field=models.FloatField(
                default=0.0, help_text="열량(kcal)(1회제공량당)", null=True
            ),
        ),
        migrations.AlterField(
            model_name="foodnutrientfact",
            name="carbohydrate",
            field=models.FloatField(
                default=0.0, help_text="탄수화물(g)(1회제공량당)", null=True
            ),
        ),
        migrations.AlterField(
            model_name="foodnutrientfact",
            name="cholesterol",
            field=models.FloatField(
                default=0.0, help_text="콜레스테롤(mg)(1회제공량당)", null=True
            ),
        ),
        migrations.AlterField(
            model_name="foodnutrientfact",
            name="protein",
            field=models.FloatField(
                default=0.0, help_text="단백질(g)(1회제공량당)", null=True
            ),
        ),
        migrations.AlterField(
            model_name="foodnutrientfact",
            name="province",
            field=models.FloatField(
                default=0.0, help_text="지방(g)(1회제공량당)", null=True
            ),
        ),
        migrations.AlterField(
            model_name="foodnutrientfact",
            name="salt",
            field=models.FloatField(
                default=0.0, help_text="나트륨(mg)(1회제공량당)", null=True
            ),
        ),
        migrations.AlterField(
            model_name="foodnutrientfact",
            name="saturated_fatty_acids",
            field=models.FloatField(
                default=0.0, help_text="포화지방산(g)(1회제공량당)", null=True
            ),
        ),
        migrations.AlterField(
            model_name="foodnutrientfact",
            name="sugars",
            field=models.FloatField(
                default=0.0, help_text="총당류(g)(1회제공량당)", null=True
            ),
        ),
        migrations.AlterField(
            model_name="foodnutrientfact",
            name="trans_fat",
            field=models.FloatField(
                default=0.0, help_text="트랜스지방(g)(1회제공량당)", null=True
            ),
        ),
    ]

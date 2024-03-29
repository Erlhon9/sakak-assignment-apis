from django.db import models


class FoodNutrientFact(models.Model):
    id = models.AutoField(primary_key=True, help_text="번호")
    food_cd = models.CharField(max_length=8, help_text="식품코드", db_index=True)
    group_name = models.CharField(max_length=20, help_text="식품군")
    food_name = models.CharField(max_length=100, help_text="식품이름", db_index=True)
    research_year = models.CharField(max_length=4, help_text="조사년도", db_index=True)
    maker_name = models.CharField(
        max_length=100, help_text="지역/제조사", db_index=True
    )
    ref_name = models.CharField(max_length=100, help_text="자료출처")
    serving_size = models.FloatField(help_text="1회 제공량")
    calorie = models.FloatField(
        help_text="열량(kcal)(1회제공량당)", null=True, default=0.0
    )
    carbohydrate = models.FloatField(
        help_text="탄수화물(g)(1회제공량당)", null=True, default=0.0
    )
    protein = models.FloatField(
        help_text="단백질(g)(1회제공량당)", null=True, default=0.0
    )
    province = models.FloatField(
        help_text="지방(g)(1회제공량당)", null=True, default=0.0
    )
    sugars = models.FloatField(
        help_text="총당류(g)(1회제공량당)", null=True, default=0.0
    )
    salt = models.FloatField(
        help_text="나트륨(mg)(1회제공량당)", null=True, default=0.0
    )
    cholesterol = models.FloatField(
        help_text="콜레스테롤(mg)(1회제공량당)", null=True, default=0.0
    )
    saturated_fatty_acids = models.FloatField(
        help_text="포화지방산(g)(1회제공량당)", null=True, default=0.0
    )
    trans_fat = models.FloatField(
        help_text="트랜스지방(g)(1회제공량당)", null=True, default=0.0
    )

    def __str__(self):
        return self.food_name

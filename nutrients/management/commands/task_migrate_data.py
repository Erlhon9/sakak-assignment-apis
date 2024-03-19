from django.core.management.base import BaseCommand
import pandas as pd
from nutrients.models import FoodNutrientFact
from django.db import transaction
import warnings
warnings.filterwarnings("ignore")

from django_project.settings.base import FILE_PATH


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_name = '통합 식품영양성분DB_음식_20230715.xlsx'
        data_file = FILE_PATH / file_name

        df = pd.read_excel(data_file)
    
        with transaction.atomic():
            # TODO: '1g 미만' 처리하기
            FoodNutrientFact.objects.bulk_create([
                FoodNutrientFact(
                    id=row['NO'],
                    food_cd=row['식품코드'],
                    group_name=row['식품대분류'],
                    food_name=row['식품명'],
                    research_year=row['연도'],
                    maker_name=row['지역 / 제조사'],
                    ref_name=row['성분표출처'],
                    serving_size=row['1회제공량'],
                    calorie=row['에너지(㎉)'] if (row['에너지(㎉)'] != '-' and type(row['에너지(㎉)']) == 'float') else 0.0,
                    carbohydrate=row['탄수화물(g)'] if (row['탄수화물(g)'] != '-' and type(row['탄수화물(g)'])  == 'float') else 0.0,
                    protein=row['단백질(g)'] if (row['단백질(g)'] != '-' and type(row['단백질(g)']) == 'float') else 0.0,
                    province=row['지방(g)'] if (row['지방(g)'] != '-' and type(row['지방(g)']) == 'float') else 0.0,
                    sugars=row['총당류(g)'] if (row['총당류(g)'] != '-' and type(row['총당류(g)']) == 'float') else 0.0,
                    salt=row['나트륨(㎎)'] if (row['나트륨(㎎)'] != '-' and type(row['나트륨(㎎)']) == 'float') else 0.0,
                    cholesterol=row['콜레스테롤(㎎)'] if (row['콜레스테롤(㎎)'] != '-' and type(row['콜레스테롤(㎎)']) == 'float') else 0.0,
                    saturated_fatty_acids=row['총 포화 지방산(g)'] if (row['총 포화 지방산(g)'] != '-' and type(row['총 포화 지방산(g)']) == 'float') else 0.0,
                    trans_fat=row['트랜스 지방산(g)'] if (row['트랜스 지방산(g)'] != '-' and type(row['트랜스 지방산(g)'])  == 'float') else 0.0,
                ) for _, row in df.iterrows()
            ])

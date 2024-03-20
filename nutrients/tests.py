import json
from re import L
from urllib import response
import pytest
from django.contrib.auth.models import User
from model_bakery import baker
from rest_framework.test import APIClient, APITestCase

from nutrients.models import FoodNutrientFact

@pytest.fixture
def api_client():
    return APIClient()

pytestmark = pytest.mark.django_db

class TestFoodNutrientFact:
    def test_list(self, api_client):
        baker.make(FoodNutrientFact, _quantity=5)
        
        response = api_client.get("/api/nutrients")
        
        assert response.status_code == 200
        assert len(response.data) == 5

    def test_retrieve(self, api_client):
        food = baker.make(FoodNutrientFact)
        
        response = api_client.get(f"/api/nutrients/{food.id}")
        
        assert response.status_code == 200
        assert response.data["id"] == food.id
        
    def test_create(self, api_client):
        food = baker.prepare(FoodNutrientFact)
        expected_data = {
            "food_cd": food.food_cd,
            "group_name": food.group_name,
            "food_name": food.food_name,
            "research_year": food.research_year,
            "maker_name": food.maker_name,
            "ref_name": food.ref_name,
            "serving_size": food.serving_size,
            "calorie": food.calorie,
            "carbohydrate": food.carbohydrate,
            "protein": food.protein,
            "province": food.province,
            "sugars": food.sugars,
            "salt": food.salt,
            "cholesterol": food.cholesterol,
            "saturated_fatty_acids": food.saturated_fatty_acids,
            "trans_fat": food.trans_fat,
        }
        
        response = api_client.post(
            "/api/nutrients",
            expected_data, 
            format="json"
        )
        
        assert response.status_code == 201
        
        data = json.loads(response.content)
        
        assert data.pop("id") == 1
        assert data == expected_data
        
    def test_update(self, api_client):
        food = baker.make(FoodNutrientFact)
        expected_data = {
            "food_cd": "12345678",
            "group_name": "test",
            "food_name": "test",
            "research_year": "2021",
            "maker_name": "test",
            "ref_name": "test",
            "serving_size": 100.0,
            "calorie": 100.0,
            "carbohydrate": 100.0,
            "protein": 100.0,
            "province": 100.0,
            "sugars": 100.0,
            "salt": 100.0,
            "cholesterol": 100.0,
            "saturated_fatty_acids": 100.0,
            "trans_fat": 100.0,
        }
        
        response = api_client.put(
            f"/api/nutrients/{food.id}",
            expected_data, 
            format="json"
        )
        
        assert response.status_code == 200
        data = json.loads(response.content)
        
        assert data.pop("id") == food.id
        assert data == expected_data
        
    def test_remove(self, api_client):
        food = baker.make(FoodNutrientFact)
        
        response = api_client.delete(f"/api/nutrients/{food.id}")
        
        assert response.status_code == 204
        assert not FoodNutrientFact.objects.filter(id=food.id).exists()
        
    def test_query(self, api_client):
        for i in range(15):
            baker.make(
                FoodNutrientFact, 
                _quantity=10,
                food_name=f"test_{i}",
            )
        
        # http://localhost:8000/api/nutrients/query?food_name=test_5 과 동일
        response = api_client.get(
            "/api/nutrients/query",
            data={"food_name": "test_5"},
        )
        
        assert response.status_code == 200
        assert len(response.data) == 10
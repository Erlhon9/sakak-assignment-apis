from rest_framework import serializers

from nutrients.models import FoodNutrientFact


class FoodNutrientFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodNutrientFact
        fields = "__all__"

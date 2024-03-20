from django.shortcuts import render
from rest_framework import viewsets

from nutrients.models import FoodNutrientFact
from nutrients.serializers import FoodNutrientFactSerializer


# Create your views here.
class NutrientViewSet(viewsets.ModelViewSet):
    queryset = FoodNutrientFact.objects.all()
    serializer_class = FoodNutrientFactSerializer

    def get_queryset(self):
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def query(self, request, *args, **kwargs):
        pass

from rest_framework import viewsets
from rest_framework.response import Response

from nutrients.filters import NutrientFilterSet
from nutrients.models import FoodNutrientFact
from nutrients.serializers import FoodNutrientFactSerializer


# Create your views here.
class NutrientViewSet(viewsets.ModelViewSet):
    queryset = FoodNutrientFact.objects.all()
    serializer_class = FoodNutrientFactSerializer
    filterset_class = NutrientFilterSet

    def get_queryset(self):
        return super().get_queryset()

    def query(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

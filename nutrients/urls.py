from django.urls import path

from nutrients.views import NutrientViewSet

nutrients_urls = [
    path("api/nutrients/query", NutrientViewSet.as_view({"get": "query"})),
    path("api/nutrients", NutrientViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "api/nutrients/<int:pk>",
        NutrientViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]

from django.urls import path
from contributions.views import delete_contribution

urlpatterns= [
    path('delete-contribution/<str:pk>/',delete_contribution,name="delete-contribution"),
]
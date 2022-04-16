from django.urls import path
from contributions.views import all_activities,delete_contribution

urlpatterns= [
    path('activities/',all_activities,name="activities"),
    path('delete-contribution/<str:pk>/',delete_contribution,name="delete-contribution"),
]
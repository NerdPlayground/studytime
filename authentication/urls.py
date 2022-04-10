from django.urls import path
from authentication.views import login_study_time,logout_study_time

urlpatterns= [
    path('login/',login_study_time,name="login"),
    path('logout/',logout_study_time,name="logout"),
]
from django.urls import path
from authentication.views import access_study_time,leave_study_time

urlpatterns= [
    path('login/',access_study_time,name="login"),
    path('logout/',leave_study_time,name="logout"),
]
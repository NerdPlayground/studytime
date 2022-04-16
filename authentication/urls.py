from django.urls import path
from authentication.views import (
    register_study_time,login_study_time,
    profile,logout_study_time,update_profile
)

urlpatterns= [
    path("login/",login_study_time,name="login"),
    path("profile/<str:pk>/",profile,name="profile"),
    path("logout/",logout_study_time,name="logout"),
    path("register/",register_study_time,name="register"),
    path("update/",update_profile,name="update"),
]
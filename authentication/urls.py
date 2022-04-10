from django.urls import path
from authentication.views import (
    register_study_time,
    login_study_time,logout_study_time
)

urlpatterns= [
    path("login/",login_study_time,name="login"),
    path("logout/",logout_study_time,name="logout"),
    path("register/",register_study_time,name="register"),
]
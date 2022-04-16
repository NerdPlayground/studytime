from django.urls import path
from topics.views import topics

urlpatterns=[
    path('topics/',topics,name="topics")
]
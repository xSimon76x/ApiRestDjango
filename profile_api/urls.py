from django.urls import path
from profile_api import views

urlpatterns = [
    path('hello-django/', views.HelloApiTestView.as_view())
]

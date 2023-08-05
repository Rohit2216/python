from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_view, name='hello'),
    path('goodbye/', views.goodbye_view, name='goodbye'),
]

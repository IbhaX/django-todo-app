from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.Homeview.as_view(), name="home"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('complete/<int:pk>', views.complete, name="complete"),
]

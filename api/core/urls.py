from django.urls import path
from . import views
from .api import api

urlpatterns = [
   path('', views.frontpage, name="frontpage"),
   path('api/', api.urls),
]

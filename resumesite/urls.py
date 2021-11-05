from django.contrib import admin
from django.urls import path, include
from .views import landing_page, IndexView

urlpatterns = [
    # path('', landing_page, name='landing_page'),
    path('', IndexView.as_view(), name="home")
]

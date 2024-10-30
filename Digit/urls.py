from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.digit_reg,name='user-view-create'),
]
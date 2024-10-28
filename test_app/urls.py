from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.UserListCreate.as_view(),name='user-view-create'),
    path('<int:pk>/',views.UserRetrieveUpdateDestroy.as_view(),name='user-retrieve-update-destory')
]
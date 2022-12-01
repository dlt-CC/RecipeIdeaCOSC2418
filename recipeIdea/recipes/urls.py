from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('register/', views.add, name='add'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
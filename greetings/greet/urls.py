from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page-two/', views.page_two, name='page_two'),
    path('page-three/', views.page_three, name='page_three'),
]
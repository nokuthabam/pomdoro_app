from django.urls import path
from . import views

app_name = 'journal'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('create/', views.create_entry, name='create'),
    path('logout/', views.user_logout, name='logout'),
    path('list/', views.list_entries, name='list'),
]

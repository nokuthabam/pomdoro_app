from django.urls import path
from . import views


app_name = 'focus_timer'

# URL configuration for focus_timer app
urlpatterns = [
    path('', views.timer_view, name='timer'),
]

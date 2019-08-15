from django.urls import path
from .views import exit

app_name = 'auth_logout'

urlpatterns = [
    path('', exit, name='exit')
]

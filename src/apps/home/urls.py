from django.urls import path, include
from .views import index, addnew

app_name = 'home'

urlpatterns = [
    path('', index, name='home_page'),
    path('login/', include('src.apps.login.urls', namespace='login')),
    path('exit/', include('src.apps.logout.urls', namespace='auth_logout')),
    path('new/', addnew, name='new_page'),
]

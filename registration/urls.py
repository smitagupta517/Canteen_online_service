from django.urls import path
from .views import register


app_name = 'registration'

urlpatterns = [
    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]

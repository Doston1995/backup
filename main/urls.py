from django.urls import path
from .views import index, backup



urlpatterns = [
    path('', index, name = 'home'),
    path('backup/', backup, name = 'backup'),
]

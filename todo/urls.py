from django.urls import path, include
from .views import Indexx
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todos', Indexx, 'todo')

urlpatterns = [
    path('', include(router.urls)),
]
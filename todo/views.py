from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer


class Indexx(viewsets.ModelViewSet):
    serializer_class =TodoSerializer
    queryset = Todo.objects.all()
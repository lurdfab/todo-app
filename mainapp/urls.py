from django.urls import path
from .api import *

urlpatterns = [
    path("create/", CreateToDo.as_view(), name="create"),
    path("list/", ListToDo.as_view(), name="list"),
    path("detail/<int:pk>/", DetailToDo.as_view(), name="detail"),
    path("delete/<int:pk>/", DeleteToDo.as_view(), name="delete"),
]

from django.urls import path
from . view import *

urlpatterns = [
    path('',listar,name='listar'),
    path('crear',crear,name=crear)
]
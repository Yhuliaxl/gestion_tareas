from .models import Tareas
from django.forms import ModelForm

class TareasForm(ModelForm):
    class meta:
        model = Tareas
        fields = '__all__'

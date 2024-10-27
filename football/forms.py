from django.forms import ModelForm
from football.models import club

class clubform (ModelForm):
    class Meta:
        model = club
        fields = '__all__'

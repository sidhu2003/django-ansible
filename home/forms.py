from .models import Details
from django.forms import ModelForm

class DetailsForm(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'
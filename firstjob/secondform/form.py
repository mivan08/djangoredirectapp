from django.forms import ModelForm
from secondform.models import Detail

class DetailForm(ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'
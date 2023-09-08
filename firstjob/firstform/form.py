from django.forms import ModelForm
from firstform.models import Member

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
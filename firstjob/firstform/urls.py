from django.urls import path
from .views import FirstFormCreateView
from .views import SecondFormCreateView

urlpatterns = [
    path('', FirstFormCreateView.as_view(), name='first_form'),
    path('next=/secondform/createview/model1/<int:id>', SecondFormCreateView.as_view(), name='second_form'),
]
from django.urls import path
from .views import FirstFormCreateView
from .views import SecondFormCreateView

urlpatterns = [
    path('', FirstFormCreateView.as_view(), name='firstform'),
    path('secondform/<int:id>', SecondFormCreateView.as_view(), name='secondform'),
]
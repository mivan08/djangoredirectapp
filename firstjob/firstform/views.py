from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .models import FirstFormModel
from .models import SecondFormModel

class FirstFormCreateView(CreateView):
 
    # specify the model for create view
    model = FirstFormModel
 
    # specify the fields to be displayed
 
    fields = ['firstname', 'lastname']

    def form_valid(self, form):
        # Save the form data and get the created object
        self.object = form.save()
        # Redirect to a success URL or return an HttpResponse
        return super().form_valid(form)

    def get_success_url(self):
        # Construct the URL for the next page with the saved object's ID
        return reverse('second_form', args=[self.object.id])


class SecondFormCreateView(CreateView):
 
    # specify the model for create view
    model = SecondFormModel
 
    # specify the fields to be displayed
 
    fields = ['address', 'hobby']

    def form_valid(self, form):
        # Save the form data and get the created object
        self.object = form.save()
        # Redirect to a success URL or return an HttpResponse
        return super().form_valid(form)

    def get_success_url(self):
        # Construct the URL for the next page with the saved object's ID
         return reverse('first_form')
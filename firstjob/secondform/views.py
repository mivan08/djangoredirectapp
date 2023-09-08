from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import DetailForm

def secondform(request, id):
     # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = DetailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            obj = form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DetailForm()

    return render(request, "secondform.html", {"form": form})
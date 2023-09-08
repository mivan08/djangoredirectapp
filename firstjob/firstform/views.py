from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import MemberForm

def firstform(request):
     # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = MemberForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            obj = form.save()
            redirect_url = f'/createview/firstmodel/{obj.id}'
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(redirect_url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MemberForm()

    return render(request, "firstform.html", {"form": form})
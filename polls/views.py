from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AuthForm
import boto3

def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print("Username: " + username + " Password: " + password)
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table('Users')
            table.put_item(
                Item={
                    'Username': username,
                    'Password': password,
                }
            )
            return HttpResponseRedirect('/polls/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthForm()

    context = {
        'name': 'Yado',
        'form': form
    }
    return render(request, 'index.html', context=context)

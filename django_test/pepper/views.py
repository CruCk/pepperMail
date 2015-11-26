from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def search_form(request):
	return render(request, 'search_form.html')
def search(request):
	if 'a' in request.GET:
		message = 'You searched for: %r'%request.GET['a']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)
def registration(request):
	return render(request, 'create-account.html')


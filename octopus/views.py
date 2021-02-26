from django.shortcuts import render

# Create your views here.

def tarifs_list(request):
	return render(request, 'octopus/index.html')

from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def index(request):
	return render{request, 'index.html', context}
	return HttpResponse('Success') 
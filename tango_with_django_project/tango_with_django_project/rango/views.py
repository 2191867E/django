from django.shortcuts import render
from django.http import HttpResponse
from rango.forms import CategoryForm


def add_category(request):
	form = CategoryForm()
	
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		
		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print(form.errors)
	return render(request,'rango/add_category.html',{'form':form})


def index(request):
    context_dict = {'boldmessage': 'Crunchy,creamy,cookie,candy,cupcake!'}
    return render(request,'rango/index.html',context = context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page <br/><a href='/rango/'>Index</a>")
    ahref='/rango/'



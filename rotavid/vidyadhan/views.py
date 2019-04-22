from django.shortcuts import render
from django.views.generic import TemplateView
from 


# Create your views here.

def IndexPage(TemplateView):
	if request.method == "POST":
		
		Ano=request.POST.get('Ano')
		Sname=request.POST.get('Sname')
		Sphoto=request.POST.get('Sfileupload')
		Fname=request.POST.get('Fname')
		Fphoto=request.POST.get('Fphoto')
		Mname=request.POST.get('Mname')
		Mphoto=request.POST.get('Mfileupload')
		School=request.POST.get('School')
		Grade=request.POST.get('Grade')
		PYmarks=request.POST.get('PYmarks')
		PPYmarks=request.POST.get('PPYmarks')
		Marks=request.POST.get('Marks')
		Incomecert=request.POST.get('Incomecert')
		Foccup=request.POST.get('Foccup')
		Moccup=request.POST.get('Moccup')
		Sfee=request.POST.get('Sfee')
		Scholar=request.POST.get('Scholar')
		new_student=Student.objects.create(title=form_title,body=form_body,cover=file)
	return render(request, "index.html")
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import View
from .models import City, Place, Plantrip
from .forms import UserForm
from django.http import JsonResponse
from django.db.models import Q



 #main website page
def frontpage(request):
	return render(request, 'places/frontpage.html')

	#user login page
class home(generic.ListView):
	template_name = 'places/home.html'
	
	def get_queryset(self):
		return Plantrip.objects.all()

#admin login page	
class IndexView(generic.ListView):
	template_name = 'places/index.html'
	
	def get_queryset(self):
		return City.objects.all()

#user cities_information 
class UserView(generic.ListView):
	
	template_name = 'places/indexuser.html'
	
	def get_queryset(self):
		return City.objects.all()
		
#admin places info and edit		
class DetailView(generic.DetailView):
	model = City
	template_name = 'places/detail.html'
	
#user places_information
class DetailuserView(generic.DetailView):
	model = City
	template_name = 'places/detailuser.html'
	
#admin Add_city
class CityCreate(CreateView):
	model = City
	fields = ['title', 'state', 'logo']
	
#admin Delete_city
def citydelete(request, city_id):
    city = City.objects.get(pk=city_id)
    city.delete()
   
    return render(request, 'places/index.html')
	
#admin Add_place
class PlaceCreate(CreateView):
	model = Place
	fields = ['city', 'place_type', 'place_title', 'description']

#admin Delete_place (not redirecting properly)
def placedelete(request, place_id):
    
    place = Place.objects.get(pk=place_id)
    place.delete()
    return render(request, 'places/placedeleted.html')
	
#registration form
class UserFormView(View):
	form_class = UserForm
	template_name = 'places/registration_form.html'
	
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form' : form})
		
	def post(self, request):
		form = self.form_class(request.POST)
		
		if form.is_valid():
			
			user = form.save(commit=False)
			
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			
			user = authenticate(username=username, password=password)
			
			if user is not None:
				
				if user.is_active:
					login(request, user)
					return redirect('places:login_user')
					
		return render(request, self.template_name, {'form' : form})
			
			
#user login form		
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('places:home')
            else:
                return render(request, 'places/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'places/login.html', {'error_message': 'Invalid login'})
    return render(request, 'places/login.html')
	     
#user logout
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'places/frontpage.html', context)
	
#user trip plan
class plan(generic.ListView):
	template_name = 'places/plan.html'
	
	def get_queryset(self):
		return Plantrip.objects.all()
		
#User Create Plan
	
class PlantripCreate(CreateView):
	model = Plantrip
	fields = ['placename', 'date']
	
#admin login form
def login_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        admin = authenticate(username=username, password=password)
        if admin is not None:
            if admin.is_active:
                login(request, admin)
                return redirect('places:index')
            else:
                return render(request, 'places/adminlogin.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'places/adminlogin.html', {'error_message': 'Invalid login'})
    return render(request, 'places/adminlogin.html')
	

#place deleted 
def placedeleted(request):
	return render(request, 'places/placedeleted.html')

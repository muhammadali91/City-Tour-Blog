from django.conf.urls import url
from . import views


app_name = 'places'
urlpatterns = [

	url(r'^$', views.frontpage, name='frontpage'),  #main website page
	
	url(r'^home/$', views.home.as_view(), name='home'),	#user login page
	
    url(r'^adminpanel/$', views.IndexView.as_view(), name='index'),	#admin login page
	
	url(r'^cities/$', views.UserView.as_view(), name='indexuser'),	#user cities_information 
	
	url(r'^(?P<pk>[0-9]+)/$', views.DetailuserView.as_view(), name='detailuser'), 	#user places_information
	
	url(r'^register/$', views.UserFormView.as_view(), name='register'),		#registration form
	
	url(r'^login_user/$', views.login_user, name='login_user'),		#user login form
	
	url(r'^login_admin/$', views.login_admin, name='login_admin'),	#admin login form
	
	url(r'^logout_user/$', views.logout_user, name='logout_user'),	#logout
	
	url(r'^adminpanel/place/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),	#admin places info and edit

	url(r'^city/add/$' , views.CityCreate.as_view(), name='city-add'),	#admin Add_city
	
	url(r'^(?P<city_id>[0-9]+)/delete/$', views.citydelete, name='city-delete'),	#admin Delete_city
	
	url(r'^adminpanel/place/add/$' , views.PlaceCreate.as_view(), name='place-add'),	#admin Add_place

	url(r'^adminpanel/place/(?P<place_id>[0-9]+)/delete/$', views.placedelete, name='place-delete'),	#admin Delete_place (not redirecting properly)
	
	url(r'^plan/$', views.plan.as_view(), name='plan'), #user trip plan
	
	url(r'^Plantrip/add/$' , views.PlantripCreate.as_view(), name='Plantrip-add'), #User Create Plan
	
	url(r'^placedeleted/$', views.placedeleted, name='placedeleted'), #place deleted 
	

]
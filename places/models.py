from django.db import models
from django.urls import reverse


class City(models.Model):
	title= models.CharField(max_length=100000)
	state= models.TextField()
	logo= models.FileField()
	
	def get_absolute_url(self):
		return reverse('places:detail', kwargs={'pk':self.pk})
	
	def __str__ (self):
		return self.title+ '-' + self.state
	
class Place(models.Model):
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	place_type = models.CharField(max_length=1400000000000000000)
	place_title = models.CharField(max_length=1400000000000000000)
	description = models.TextField(default='')

	def get_absolute_url(self):
		return reverse('places:index')
	
	def __str__(self):
		return self.place_title+ '-' + self.place_type

class Plantrip(models.Model):
	
		placename = models.ForeignKey(Place, on_delete=models.CASCADE)
		date = models.DateField(null=True)
		
		
		def get_absolute_url(self):
			return reverse('places:plan')
		
		def __str__(self):
			return self.placename



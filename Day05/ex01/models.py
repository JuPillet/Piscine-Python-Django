from django.db import models

# Create your models here.
class Movies(models.Model):
	title = models.CharField( max_length=64, blank=False, null=False )
	episode_nb = models.BigAutoField( primary_key=True )
	opening_crawl = models.TextField( blank=True, null=True )
	director = models.CharField( max_length=32, blank=False, null=False )
	producer = models.CharField( max_length=128, blank=False, null=False )
	release_date = models.DateField( blank=False, null=False )
	def __str__( self ):
		return self.title
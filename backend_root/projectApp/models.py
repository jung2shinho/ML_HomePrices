from django.db import models
# NOTE: Make sure to migrate after any changes on models

class House(models.Model):
	# Model Attributes
	address=models.CharField(max_length=15)
	city=models.CharField(max_length=15)
	state=models.CharField(max_length=2)
	bedrooms=models.IntegerField(default=0)
	bathrooms=models.IntegerField(default=0)
	sqft_living=models.IntegerField(default=0)
	sqft_lot=models.IntegerField(default=0)
	floors=models.IntegerField(default=1)
	latitude=models.FloatField(default=0)
	longitude=models.FloatField(default=0)
	estPrice=models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True)

	# Display string
	def __str__(self):
		return '{},{},{}'.format(self.address,self.city,self.state)

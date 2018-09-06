from django.db import models
from django.contrib.auth.models import User



class Stations(models.Model):
    fueil_level = models.IntegerField()
    station_type = models.CharField(max_length = 10,default = 'petrol')

    
    
    
    def __str__(self):
        return self.station_type
class UserProfileMode(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	station_type= models.CharField(max_length=1,choices =(('P','petrol'),('D','diesel')),blank=False)
	def __str__(self):
		return self.user.username
	class Mete:
		verbose_name = 'profile'
		verbose_name_plural = 'profiles' 


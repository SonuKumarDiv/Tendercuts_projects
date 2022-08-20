from django.db import models
class User(models.Model):
	email=models.EmailField(max_length=60, unique=True)
	username=models.CharField(max_length=30,default='')
	password=models.TextField(default="")
	user_type= models.CharField(max_length=12,default='admin')
	profile_pic=models.ImageField(upload_to='user/profile_image',default='deafult_profile_pic.jpeg')
	country_code=models.CharField(max_length=10)
	phone_number=models.CharField(max_length=15)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name','last_name','country_code','phone_number']
	def __str__(self):
		return 'ID='+str(self.id)+'user='+str(self.username)


	
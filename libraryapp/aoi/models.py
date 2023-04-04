from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import RegexValidator
 

# Create your models here.


class UserDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dob=models.DateField(null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True) 
    image=models.ImageField(upload_to="images",null=True,blank=True)

    
class Books(models.Model):
    bookname=models.CharField(max_length=200)
    isbn=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    published_on=models.DateField(null=True)
    isactive=models.BooleanField(default=False)

    def __str__(self):
        return self.bookname
    
#Userbook model is to assign a book for a perticular user

class UserBook(models.Model):
    borrower=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    assigned_on=models.DateField(auto_now_add=True)
    curdate=datetime.date.today()
    et=curdate+datetime.timedelta(days=14)
    returndate=models.DateField(default=et,null=True) #by default there is an return date assigned that is 14 days

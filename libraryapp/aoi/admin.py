from django.contrib import admin
from aoi .models import Books,UserDetails,UserBook

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Books)
admin.site.register(UserBook)

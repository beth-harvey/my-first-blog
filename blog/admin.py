from django.contrib import admin
from .models import Post #this imports the Post model that we created 


#register your models here
admin.site.register(Post) #this registers the Post model and makes it visible on the admin page
from django.contrib import admin

# Register your models here.
from .models import Movie,Show,Booking

admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(Booking)
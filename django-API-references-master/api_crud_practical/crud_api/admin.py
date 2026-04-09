from django.contrib import admin
from .models import Student


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']


#   [or] can be done like below:-

# admin.site.register(Student)


##  // But in both approaches, the view in 'Admin' Panel will be a bit different.
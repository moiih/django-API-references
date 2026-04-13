from my_api.models import Language
from django.contrib import admin

# Register your models here.

# @admin.register(Language)     ## If we are using this '@admin.register(model_name)' decorator then don't use "admin.site.register(model_name)" becz it is itself registering the model using itself (decorator way to register model).
# class LanguageAdmin(admin.ModelAdmin):
#     '''Admin View for Language'''

#     list_display = ('name', 'paradigm',)
    


admin.site.register(Language)
# admin.site.register(Language, LanguageAdmin)  ## Use this approach when we are using this 'LanguageAdmin' class(user-defined) 
#                                               ## but don't include this '@admin.register()' decorator.
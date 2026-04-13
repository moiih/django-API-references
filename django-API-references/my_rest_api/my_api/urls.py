from django.urls import path, include
from . import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register('languages', views.LanguageView)    ## This 'languages' in the arguments is the "URL_PATH" for our API (just like we specify path in "url_patterns")

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('hello-api/', views.hello_api, name='hello_api'),
]

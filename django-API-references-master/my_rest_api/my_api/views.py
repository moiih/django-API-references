from django.shortcuts import render
from django.http import HttpResponse
from .models import Language

import json
from django.core import serializers
from django.forms.models import model_to_dict

from .serializers import LanguageSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView

# Create your views here.

# class LanguageView(viewsets.ModelViewSet):
#     queryset = Language.objects.all()
#     serializer_class = LanguageSerializer
#     # permission_classes = (permissions.IsAuthenticated,)   ## "permission.IsAuthenticatedOrReadOnly" for Read Only Mode.





@api_view()
def hello_api(request):

    lang = Language.objects.get(id=1)

    # assuming obj is your model instance
    # dict_obj = model_to_dict( lang )

    # serialized = json.dumps(lang)

    serialzed_data = serializers.serialize("json", Language.objects.all())
    print('\n\n', serialzed_data, end='\n\n')
    json_data = {"SomeModel_json": serialzed_data}
    print('\n\n', json_data, end='\n\n')

    # return Response(lang)
    # return Response(dict_obj)
    # return Response(serialized)
    # return Response(serialzed_data)    
    return Response(json_data)    

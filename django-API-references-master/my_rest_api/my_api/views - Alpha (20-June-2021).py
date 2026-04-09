from django.shortcuts import render
from .models import Language

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
    return Response({"message": "Hello, world!"})






@api_view()
def hello_api(request):

    lang = Language.objects.get(id=1)

    # print('\n\nLang :', lang, end='\n\n')

    # object_list = []
    # for obj in lang:
    #     object_list.append(obj)
    
    # json_data = json.dumps(object_list)

    # lang = serializers.serialize('xml', Language.objects.all(), fields=('name','paradigm'))
    json_data = serializers.serialize('json', [ lang, ])    
    struct = json.loads(json_data)
    data = json.dumps(struct[0])
    return HttpResponse(data)


    # assuming obj is your model instance
    # dict_obj = model_to_dict( lang )

    # serialized = json.dumps(dict_obj)

    # return Response(lang)
    # return Response(dict_obj)





# class Logout(APIView):
#     def get(self, request, format=None):
#         # simply delete the token to force a login
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
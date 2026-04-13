from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer

import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


# Create your views here. 

# Class-based approach

# @method_decorator(csrf_exempt, name='dispatch')
# class StudentAPI(View):

#     def get(self, request, *args, **kwargs):

#         json_data = request.body    # Getting the data in the 'request' in 'JSON' Format
#         print('\n\nJSON_Data: ',json_data, end='\n\n')
#         stream = io.BytesIO(json_data)  # Converting the obtained data into a 'stream'
#         print('\n\nStream: ', stream, end='\n\n')
#         pythondata = JSONParser().parse(stream) # Now converting this stream into the data-type that can be read by Python
#         print('\n\nStream: ', pythondata, end='\n\n')
#         id = pythondata.get('id', None)     # Here, we are storing the data inside the 'pythondata' into another variable 'id'.
#                                             # In "...get('id', None)", we are saying that if the data inside 'pythondata' 
#                                             # is not 'None' then 'get' the value, else 'get' 'None'(empty Json).
        
#         if id is not None:
#             stu = Student.objects.get(id=id)            
#             serializer = StudentSerializer(stu, many=False)     # By default, "many" is set to "False"
#             json_data = JSONRenderer().render(serializer.data)

#             return HttpResponse(json_data, content_type='application/json')

#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)

#         return HttpResponse(json_data, content_type='application/json')




#     def post(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)

#         serializer = StudentSerializer(data = python_data)

#         if serializer.is_valid():
#             serializer.save()
#             success_response = { 'create-status': 'success' }
#             json_response = JSONRenderer().render(success_response)

#             return HttpResponse(json_response, content_type='application/json')

#         error_response = serializer.errors
#         json_response = JSONRenderer().render(serializer.errors)

#         print('n\nSerializer Errors : \n', serializer.errors, end='\n\n')

#         return HttpResponse(json_data, content_type='application/json')




#     def put(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')   # This time we will only pass 'id' and not 'None' becz there is no data exists with 'id=None'. 
#                                     # So some 'id' is a must.

#         stu = Student.objects.get(id=id)            
#         serializer = StudentSerializer(stu, data=pythondata, partial=True)  # "partial=True" for a combined (PUT / PATCH) method.
#         # For pure "PUT" request method just remove 'partial=True' from above statement.
#         # For pure "PATCH" request method just add 'partial=True' from above statement

#         if serializer.is_valid():
#             serializer.save()
#             success_response = {
#                 'update-status': 'success'
#             }
#             json_response = JSONRenderer().render(success_response)

#             return HttpResponse(json_response, content_type='application/json')

#         error_response = serializer.errors
#         json_response = JSONRenderer().render(serializer.errors)

#         return HttpResponse(json_data, content_type='application/json')




#     def delete(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')

#         stu = Student.objects.get(id=id)
#         stu.delete()

#         success_response = {
#             'delete-status': 'success'
#         }
#         json_response = JSONRenderer().render(success_response)

#         return HttpResponse(json_response, content_type='application/json')







@csrf_exempt
def student_api(request):

    print('\n\nRequest_Data:', request, end='\n\n')
    print('\n\nRequest_Data:', request.body, end='\n\n')

    # For getting data from the database from API    
    if request.method == 'GET':
        json_data = request.body    # Getting the data in the 'request' in 'JSON' Format
        stream = io.BytesIO(json_data)  # Converting the obtained data into a 'stream'
        pythondata = JSONParser().parse(stream) # Now converting this stream into the data-type that can be read by Python
        id = pythondata.get('id', None)     # Here, we are storing the data inside the 'pythondata' into another variable 'id'.
                                            # In "...get('id', None)", we are saying that if the data inside 'pythondata' 
                                            # is not 'None' then 'get' the value, else 'get' 'None'(empty Json).
        
        if id is not None:
            stu = Student.objects.get(id=id)            
            serializer = StudentSerializer(stu, many=False)     # By default, "many" is set to "False"
            json_data = JSONRenderer().render(serializer.data)

            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)

        return HttpResponse(json_data, content_type='application/json')




    # For creating data in the database through API
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        serializer = StudentSerializer(data = python_data)

        if serializer.is_valid():
            serializer.save()
            success_response = { 'create-status': 'success' }
            json_response = JSONRenderer().render(success_response)

            return HttpResponse(json_response, content_type='application/json')

        error_response = serializer.errors
        json_response = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data, content_type='application/json')




    # For updating data in the database through API
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')   # This time we will only pass 'id' and not 'None' becz there is no data exists with 'id=None'. 
                                    # So some 'id' is a must.

        stu = Student.objects.get(id=id)            
        serializer = StudentSerializer(stu, data=pythondata, partial=True)  # "partial=True" for a combined (PUT / PATCH) method.
        # For pure "PUT" request method just remove 'partial=True' from above statement.
        # For pure "PATCH" request method just add 'partial=True' from above statement

        if serializer.is_valid():
            serializer.save()
            success_response = {
                'update-status': 'success'
            }
            json_response = JSONRenderer().render(success_response)

            return HttpResponse(json_response, content_type='application/json')

        error_response = serializer.errors
        json_response = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data, content_type='application/json')



    # For deleting data from the database using API
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')

        stu = Student.objects.get(id=id)
        stu.delete()

        success_response = {
            'delete-status': 'success'
        }
        json_response = JSONRenderer().render(success_response)

        return HttpResponse(json_response, content_type='application/json')

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from  .serializers import TaskSerializer
from .models import Task


# Create your views here.



# ## Using this "get_object_or_404( model_name, pk=primary_key_argument )" 
# ## is equivalent to this following code.

# from django.http import Http404

# def my_view(request):
#     try:
#         obj = MyModel.objects.get(pk=1)
#     except MyModel.DoesNotExist:
#         raise Http404("No MyModel matches the given query.")



def basic_json_response(request):
    return JsonResponse("This is a basic JSON Response", safe=False)



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
		'List':'http://127.0.0.1:8080/api/task-list/',
		'Detail View':'http://127.0.0.1:8080/api/task-detail/<str:pk>/',
		'Create':'http://127.0.0.1:8080/api/task-create/',
		'Update':'http://127.0.0.1:8080/api/task-update/<str:pk>/',
		'Delete':'http://127.0.0.1:8080/api/task-delete/<str:pk>/',
	}

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()    
    serializer = TaskSerializer(tasks, many=True)   ## ["many=True"] only when many reords are to be fetched.
    serialized_data = serializer.data

    return Response(serialized_data)


@api_view(['GET'])
def taskDetail(request, pk):
    # task_detail = Task.objects.get(id=pk)
    task_detail = get_object_or_404(Task, pk=pk)  ## This will not show any error, instead, it will show a sweet "{ "detail": "Not found." }" as Response (and that too in JSON Format).
    serializer = TaskSerializer(task_detail, many=False)    ## ["many=True"] when only on single record is to be fetched.
    serialized_data = serializer.data

    return Response(serialized_data)



@api_view(['GET'])
def taskDelete(request, pk):
    # task = Task.objects.get(id=pk)    ## This works well but it produces an "Django Error Message Page" which is not likely.
    task = get_object_or_404(Task, pk=pk)   ## This does not display the error page, instead, it shows "{ "details": "Not found" } as Response in JSON Format.
    task.delete()

    delete_response_message = {
        # 'delete-message' : 'Item Successfully Deleted!!',
        'delete-status' : 'success'
    }

    return Response(delete_response_message)



@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    serialized_data = serializer.data

    return Response(serialized_data)



@api_view(['PUT'])      # We can also used "POST" request also (like, @api_view(['POST'])) and this would also work, but to make it purely for 'updating' purpose, 'PUT' is more suitable.
def taskUpdate(request, pk):        ## The "UPDATE" means that the whole row(record) in the database is to be changed.
    task = Task.objects.get(pk=pk)
    # task = get_object_or_404(Task, pk=pk)   ## This does not display the error page, instead, it shows "{ "details": "Not found" } as Response in JSON Format.
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['PATCH'])        # We can also used "POST" request also (like, @api_view(['POST'])) and this would also work, but to make it purely for 'updating some specific fields only and not affecting the other fields', 'PATCH' is more suitable option.
def taskPatch(request, pk):           ## The "PATCH" means the data of some particular field(s) is to be changed.
    # task = Task.objects.get(pk=pk)  
    task = get_object_or_404(Task, pk=pk)   ## This does not display the error page, instead, it shows "{ "details": "Not found" } as Response in JSON Format.
    serializer = TaskSerializer(task, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

    serialized_data = serializer.data

    return Response(serialized_data)


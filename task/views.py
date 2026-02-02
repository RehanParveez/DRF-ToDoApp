# from rest_framework.decorators import api_view, permission_classes
# from task.models import Task
# from task.serializers import TaskSerializers, UserSerializer
# from task.permissions import IsOwnerOrReadOnly
# from rest_framework.exceptions import PermissionDenied
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
# from django.contrib.auth.models import User
# from rest_framework.response import Response

# # Create your views here.

# # Task Related views

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def task_list(request):

#  #this is about listing all tasks, or creating a new one  
#    if request.method == "GET":
#        tasks = Task.objects.filter(user=request.user)
#        serializer = TaskSerializers(tasks, many=True)
#        return Response(serializer.data)
   
#    elif request.method == "POST":
#         serializer = TaskSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
# def task_detail(request, pk):

# this is aout retrieving, updating or deleting a task. and also here the object-level permissions are being handled by IsOwnerOrReadOnly.

#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     # here we are checking the object-level permission manually for FBV
#     permission = IsOwnerOrReadOnly()
#     if request.method in ['PUT', 'DELETE']:
#         if not permission.has_object_permission(request, None, task):
#             raise PermissionDenied("you don't have permission to edit the task")

#     if request.method == "GET":
#         serializer = TaskSerializers(task)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = TaskSerializers(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # User related views
# @api_view(['GET'])
# @permission_classes([IsAdminUser])
# def user_list(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_detail(request):
#     serializer = UserSerializer(request.user)
#     return Response(serializer.data)
 
   

# Class Based Views:

# Views For Task
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
# from rest_framework.exceptions import PermissionDenied
# from django.contrib.auth.models import User
# from task.models import Task
# from task.serializers import TaskSerializers, UserSerializer
# from task.permissions import IsOwnerOrReadOnly

# Views for Users

# class TaskList(APIView):
#     # this is about listing all tasks for the logged in user or creating a new task
#     permission_classes = [IsAuthenticatedOrReadOnly]
    
#     def get(self, request):
#         tasks = Task.objects.filter(user=request.user)
#         serializers = TaskSerializers(tasks, many=True)
#         return Response(serializers.data)
    
#     def post(self, request):
#         serializer = TaskSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
# class TaskDetail(APIView):
#     # this is aout retrieving, updating or deleting a task. and also here the object-level permissions are being handled by IsOwnerOrReadOnly.
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         try:
#             return Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             raise PermissionDenied("Task is not found or you dont have the access")

#     def get(self, request, pk):
#         task = self.get_object(pk)
#         serializer = TaskSerializers(task)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         task = self.get_object(pk)
#         # Check object-level permission
#         permission = IsOwnerOrReadOnly()
#         if not permission.has_object_permission(request, None, task):
#             raise PermissionDenied("You can't edit this task")
        
#         serializer = TaskSerializers(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         task = self.get_object(pk)
#         # Check object-level permission
#         permission = IsOwnerOrReadOnly()
#         if not permission.has_object_permission(request, None, task):
#             raise PermissionDenied("You can't delete this task")
        
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # User Views

# class UserList(APIView):
#    # Listing all the users with admin control
#     permission_classes = [IsAdminUser]

#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

# class UserDetail(APIView):
#     # Returing the data of the currently logged-in user
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)


# Writing views using Viewsets()

from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from task.models import Task
from task.serializers import TaskSerializers, UserSerializer
from task.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action


class TaskViewSet(viewsets.ModelViewSet):
    # this will automatically generate the functionality for retrieving, updating or deleting a task. and also here the object-level permissions are being handled by IsOwnerOrReadOnly.
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # this will automatically generate us the list and detail functionality
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def user_detail(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    
    
    


    

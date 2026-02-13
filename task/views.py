# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from task.models import Task
# from task.serializers import TaskSerializers, UserSerializer
# from task.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
# from rest_framework.exceptions import PermissionDenied
# from rest_framework import status
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# from rest_framework.authtoken.models import Token
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
# from django.contrib.auth.models import User
# from rest_framework.response import Response

# # Create your views here.

# # Task Related views

# @api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication, SessionAuthentication, JWTAuthentication])
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
# @authentication_classes([TokenAuthentication, SessionAuthentication, JWTAuthentication])
# @permission_classes([IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
# def task_detail(request, pk):
# # this is aout retrieving, updating or deleting a task. and also here the object-level permissions are being handled by IsOwnerOrReadOnly.

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

# @api_view(['POST'])
# @permission_classes([permissions.AllowAny])
# def generate_token(request):
#     username = request.data.get('username')

#     if not username:
#         return Response(
#             {'error': 'username is required'},
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist:
#         return Response(
#             {'error': 'user is not found'},
#             status=status.HTTP_404_NOT_FOUND
#         )

#     token, created = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key})

# @api_view(['GET'])
# @permission_classes([IsAdminUser])
# def user_list(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# @authentication_classes([TokenAuthentication, SessionAuthentication, JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def user_detail(request):
#     serializer = UserSerializer(request.user)
#     return Response(serializer.data)
 
   

# # Class Based Views:

# # Views For Task
# from rest_framework.views import APIView
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
# from rest_framework import permissions
# from rest_framework.exceptions import PermissionDenied
# from django.contrib.auth.models import User
# from task.models import Task
# from task.serializers import TaskSerializers, UserSerializer
# from task.permissions import IsOwnerOrReadOnly

# # Views for Users

# class TaskList(APIView):
#     # this is about listing all tasks for the logged in user or creating a new task
#     authentication_classes = [TokenAuthentication, SessionAuthentication]
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
#     authentication_classes = [TokenAuthentication, SessionAuthentication]
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

# class GenerateTokenAPIView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         username = request.data.get('username')

#         if not username:
#             return Response(
#                 {'error': 'username is required'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             return Response(
#                 {'error': 'user is not found'},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})

# class UserList(APIView):
#    # Listing all the users with admin control
#     permission_classes = [IsAdminUser]

#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

# class UserDetail(APIView):
#     # Returing the data of the currently logged-in user
#     authentication_classes = [TokenAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)



# Writing views using generic class based views()

# Task Related Views:

# from rest_framework.views import APIView            # this import was being used for generate token view  
# from rest_framework import mixins
# from rest_framework import generics
# from task.pagination import TaskPagination
# from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
# from rest_framework.authtoken.models import Token   # this import was being used for generate token view
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from task.throttles import TaskCreateThrottle, AuthThrottle
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.response import Response        # this import was being used for generate token view
# from rest_framework import status                   # this import was being used for generate token view 
# from rest_framework import permissions
# from task.models import Task
# from task.serializers import TaskSerializers, UserSerializer
# from task.permissions import IsOwnerOrReadOnly
# from django.contrib.auth.models import User

# class TaskListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     authentication_classes = [TokenAuthentication, SessionAuthentication, JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     serializer_class = TaskSerializers
#     pagination_class = TaskPagination
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
#     # fileds to filter here
#     filter_fields = ['status']
#     search_fields = ['title']
#     ordering_fields = ['created_at']
#     ordering = ['created_at']
    
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    
#     def get_queryset(self):
#        if not self.request.user.is_authenticated:
#           return Task.objects.none()
#        return Task.objects.filter(user=self.request.user)
    
#     def perform_create(self, serializer):
#         task = serializer.save(user=self.request.user)
#         # storing the last created task in the session
#         self.request.session['last_created_task'] = task.id
#         print(f'user {self.request.user.username} created task {task.id}')
        
#     def get_throttles(self):
#         if self.request.method == 'POST':
#             return [TaskCreateThrottle()]
#         return super().get_throttles()
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class TaskDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Task.objects.all()
#     authentication_classes = [TokenAuthentication, SessionAuthentication, JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     serializer_class = TaskSerializers
    
#     def get(self, request, *args, **kwargs):
#         response = self.retrieve(request, *args, **kwargs)
#         # storing the last visited task in the session
#         task_id = self.get_object().id
#         request.session['last_visited_task'] = task_id
#         print(f'user {request.user.username} visited this task {task_id}')

#         return response
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
# # User Related Views

# class ThrottledTokenObtainPairView(TokenObtainPairView):
#     throttle_classes = [AuthThrottle]

# class GenerateTokenView(APIView):
#     permission_classes = [permissions.AllowAny]
    
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         if not username:
#             return Response({'error': 'username is required'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             return Response({'error': 'user is not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})

# class UserListView(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = User.objects.all()
#     permission_classes = [permissions.IsAdminUser]
#     serializer_class = UserSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
#     filter_fields = ['username', 'email']
#     search_fields = ['username', 'email']
#     ordering_fields = ['id', 'username']
#     ordering = ['id']   
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
# class UserDetailView(generics.RetrieveAPIView):
#     authentication_classes = [TokenAuthentication, SessionAuthentication, JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = UserSerializer
    
#     def get_object(self):
#         return self.request.user
   
    

# # Writing views using Viewsets()

from rest_framework import viewsets
from rest_framework import permissions
# from rest_framework.parsers import JSONParser, FormParser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from task.models import Task
from task.serializers import TaskSerializers, UserSerializer
from task.permissions import IsOwnerOrReadOnly

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    # parser_classes = [JSONParser, FormParser]
    authentication_classes = [TokenAuthentication, SessionAuthentication, JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated():
            return Task.objects.none
        return Task.objects.filter(user=user).select_related('user')
    # assigning the user automatically during the creation
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    # the permission that only admin can delete 
    def get_permissions(self):
        if self.action == 'destroy':
            return [permissions.IsAdminUser()]
        return [permission() for permission in self.permission_classes]
    
    # creating the action to mark the task like its done
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def mark_done(self, request, pk=None):
        task = self.get_object()
        task.status = 'completed'
        task.save()
        return Response({'message': 'task is done', 'task_id': task.id})
    
    # creating the stats about the tasks 
    @action(detail=False, methods=['get'])
    def stats(self,  request):
        queryset = self.get_queryset()
        total = queryset.count()
        completed = queryset.filter(status='completed').count()
        pending = queryset.filter(status='pending').count()
        
        return Response({"total_tasks": total, "completed_tasks": completed, "pending_tasks": pending})
        
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # this will automatically generate us the list and detail functionality
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def user_detail(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    


    

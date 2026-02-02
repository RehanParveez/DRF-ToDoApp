# Function Based Urls
# from django.urls import path
# from task.views import task_list, task_detail, user_list, user_detail

# urlpatterns = [
#     path('tasklist/', task_list),
#     path('taskdetail/<int:pk>/', task_detail),
#     path('userlist/', user_list),
#     path('userdetail/', user_detail),
# ]


# Class Based Urls
# from django.urls import path
# from task.views import TaskList, TaskDetail, UserList, UserDetail

# urlpatterns = [
#    path('tasklist/', TaskList.as_view()),
#    path('taskdetail/<int:pk>/', TaskDetail.as_view()),
#    path('userlist/', UserList.as_view()),
#    path('userdetail/', UserDetail.as_view()),
# ]


# Router Based Urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task.views import TaskViewSet, UserViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]






# # Function Based Urls
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from task.views import task_list, task_detail, user_list, user_detail, generate_token

# urlpatterns = [
#     path('tasklist/', task_list),
#     path('taskdetail/<int:pk>/', task_detail),
#     path('userlist/', user_list),
#     path('userdetail/', user_detail),
#     path('generatetoken/', generate_token),       # this urls was being used for the token generation inside the tokenauthentication
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

# Class Based Urls
# from django.urls import path
# from task.views import TaskList, TaskDetail, UserList, UserDetail, GenerateTokenAPIView

# urlpatterns = [
#    path('tasklist/', TaskList.as_view()),
#    path('taskdetail/<int:pk>/', TaskDetail.as_view()),
#    path('userlist/', UserList.as_view()),
#    path('userdetail/', UserDetail.as_view()),
#    path('generatetoken/', GenerateTokenAPIView.as_view()),
# ]



# Generic Class based Views based Urls

# from django.urls import path
# from task.views import TaskListView, TaskDetailView, UserListView, UserDetailView, GenerateTokenView, ThrottledTokenObtainPairView
# from rest_framework_simplejwt.views import TokenRefreshView


# urlpatterns = [
#    path('tasklist/', TaskListView.as_view()),
#    path('taskdetail/<int:pk>/', TaskDetailView.as_view()),
#    path('userlist/', UserListView.as_view()),
#    path('userdetail/', UserDetailView.as_view()),
#    path('generatetoken/', GenerateTokenView.as_view()),
# #    path('tokenobtain/', TokenObtainPairView.as_view()), # the ThrottledTokenObtainPairView related urls is replacement for this url
#    path('tokenrefresh/', TokenRefreshView.as_view()),
#    path('throttletokenobtain/', ThrottledTokenObtainPairView.as_view())
# ]


# Router Based Urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task.views import TaskViewSet, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
   # URL Versioning
    path('api/v1/', include(router.urls)),
    path('api/v1/tokenobtain/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/v1/tokenrefresh/', TokenRefreshView.as_view(), name='token_refresh'),
]







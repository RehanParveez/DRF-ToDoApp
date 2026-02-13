# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from task.models import Task

class TaskAPITestCase(APITestCase):

    def setUp(self):
        # Creating users
        self.user1 = User.objects.create_user(username='user1', password='user112312')
        self.user2 = User.objects.create_user(username='user2', password='user212312')

        # Creating tasks for user1
        self.task1 = Task.objects.create(user=self.user1, title='Task1', description='descr1', status='completed')
        self.task2 = Task.objects.create(user=self.user1, title='Task2', description='descr2', status='pending')
        self.client = APIClient()

        # getting the jwt token for the user1
        response = self.client.post('/task/api/v1/tokenobtain/', {'username': 'user1', 'password': 'user112312'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
   
    # list of task test
   
    def test_task_list(self):
        response = self.client.get('/task/api/v1/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # creating task
    
    def test_task_create(self):
        data = {'title': 'Task3', 'description': 'desc3', 'status': 'pending'}
        response = self.client.post('/task/api/v1/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.filter(user=self.user1).count(), 3)
  
    # retrieving the task
    def test_task_retrieve(self):
        response = self.client.get(f'/task/api/v1/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task1.title)

  # update task
    def test_task_update(self):
        data = {'title': 'Task1 Updated', 'status': 'completed'}
        response = self.client.patch(f'/task/api/v1/tasks/{self.task1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Task1 Updated')

    # owner related test
    
    def test_user_cannot_access_other_user_task(self):
        # logging in as user2
        response = self.client.post('/task/api/v1/tokenobtain/', {'username': 'user2','password': 'user212312'}, format='json')
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # accessing user1's task
        response = self.client.get(f'/task/api/v1/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        
            
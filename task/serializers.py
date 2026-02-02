from rest_framework import serializers
from task.models import Task
from django.contrib.auth.models import User

class TaskSerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'user', 'status', 'created_at']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
        

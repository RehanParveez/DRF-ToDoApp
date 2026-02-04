from rest_framework import serializers
from task.models import Task
from django.contrib.auth.models import User

class TaskSerializers(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'owner', 'status', 'created_at']
        read_only_fields = ['id', 'owner', 'created_at']
        
    def get_owner(self, obj):
        return obj.user.username
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        read_only_fields = ['id', 'email']
        
        

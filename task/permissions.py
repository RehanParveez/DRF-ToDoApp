from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    
    # this is a custom permission to allow only the user to edit their tasks
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

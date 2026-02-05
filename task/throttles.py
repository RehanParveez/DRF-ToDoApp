from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class TaskCreateThrottle(UserRateThrottle):
    scope = 'task_create'
    
class AuthThrottle(AnonRateThrottle):
    scope = 'auth'
    

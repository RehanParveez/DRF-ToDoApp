from django.utils import timezone

class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # this part is before the view executes 
        user = request.user
        method = request.method
        path = request.path
        
        if user.is_authenticated:
            print(f'User: {user.username} | Method: {method} | Path: {path}')
        else:
            print(f'Anonymous | Method: {method} | Path: {path}')
            
        response = self.get_response(request)
        # this part is after the view executes 
        if user.is_authenticated:
            request.session['last_activity'] = str(timezone.now())
            print(f'the last activity which is saved for {user.username}')
            
        # adding the custom response header
        response['X-App-Name'] = 'DRF-ToDo-App'
        return response
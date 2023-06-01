from datetime import datetime
from django.utils.deprecation import MiddlewareMixin

from django.contrib.auth import get_user_model

User = get_user_model()
           

class CheckRequestMiddleware(MiddlewareMixin):
    
    def process_response(self, request, response):
        if request.user.is_authenticated:
            current_user = User.objects.get(id=request.user.id)
            current_user.last_request = datetime.now()
            current_user.save()
        return response

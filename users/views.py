from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.utils.decorators import method_decorator

from .models import User


@method_decorator(login_required, name='dispatch')
class UserDetailView(DetailView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserDetailView, self).dispatch(*args, **kwargs)
            
    model = User
    
    
    

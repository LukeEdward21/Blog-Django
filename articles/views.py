from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, FormView
from django.shortcuts import render, redirect

from .forms import WriteForm
from .models import Article



@method_decorator(login_required, name='dispatch')
class ArticleFormView(FormView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArticleFormView, self).dispatch(*args, **kwargs)
    
    model = Article
    template_name = 'articles/write.html'
    success_url = '/'
    form_class = WriteForm


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_writer:
            raise Http404("Página não existe!")
        return super(ArticleFormView, self).get(request, *args, **kwargs)

'''
@login_required
def article_form_view(request):
    if request.user.is_writer:
        if request.method == 'POST':
            form = WriteForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = WriteForm()
            # form.fields['author'] = request.user

        return render(request, 'articles/write.html', {'form': form})
    raise Http404("Página não existe!")
'''

class ArticleListView(ListView):
    paginate_by = 6
    model = Article


class ArticleDetailView(DetailView):
    model = Article



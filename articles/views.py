from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import WriteForm
from .models import Article


@method_decorator(login_required, name='dispatch')
class ArticleCreateView(CreateView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArticleCreateView, self).dispatch(*args, **kwargs)
    
    model = Article
    template_name = 'articles/write.html'
    success_url = '/'
    success_message = ''
    form_class = WriteForm


    def form_valid(self, form):
        try:
            obj = form.save(commit=False)
            obj.author = self.request.user
            obj.save()
            messages.success(self.request, "Artigo salvo com sucesso!")
            return super().form_valid(form)
        except Exception as e:
            messages.warning(self.request, "Problema ao salvar o artigo!")
            return super(ArticleCreateView, self)
        
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_writer:
            raise Http404("Página não existe!")
        return super(ArticleCreateView, self).get(request, *args, **kwargs)


class ArticleListView(ListView):
    paginate_by = 6
    model = Article


class ArticleDetailView(DetailView):
    model = Article


@method_decorator(login_required, name='dispatch')
class UpdateArticleView(UpdateView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateArticleView, self).dispatch(*args, **kwargs)
    
    model = Article
    template_name = 'articles/edit.html'
    form_class = WriteForm
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_writer:
            raise Http404("Página não existe!")
        
        return super(UpdateArticleView, self).get(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class DeleteArticlesView(DeleteView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteArticlesView, self).dispatch(*args, **kwargs)
    
    model = Article
    template_name = 'articles/delete.html'
    success_url = '/'
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_writer:
            raise Http404("Página não existe!")
        
        return super(DeleteArticlesView, self).get(request, *args, **kwargs)
    
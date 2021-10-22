from django.contrib.auth.decorators import login_required
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
        form.save()
        return super().form_valid(form)        


class ArticleListView(ListView):
    paginate_by = 6
    model = Article


class ArticleDetailView(DetailView):
    model = Article



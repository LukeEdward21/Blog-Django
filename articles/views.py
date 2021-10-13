from django.views.generic import DetailView, ListView

from .models import Article


class ArticleListView(ListView):
    paginate_by = 6
    model = Article


class ArticleDetailView(DetailView):
    model = Article
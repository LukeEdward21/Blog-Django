from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="list"),
    path("<slug:slug>/", views.ArticleDetailView.as_view(), name="detail"),
    path("articles/write/", views.ArticleFormView.as_view(), name="write"),
    # path("articles/write/", views.article_form_view, name="write"),
]
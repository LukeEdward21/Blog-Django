from django.urls import path

from .views import UserDetailView


app_name = 'users'

urlpatterns = [
    # path("users/edit-profile", views.ArticleFormView.as_view(), name="write"),
    path('users/<slug:slug>', UserDetailView.as_view(), name="user-profile"),
]

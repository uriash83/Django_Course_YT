from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView)
from . import  views

urlpatterns = [
    #path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #pk - primary key
    path('post/new/', PostCreateView.as_view(), name='post-create'), # template dla tego to nie post-create tylko post_form zgodnie z <model>_<viewtype>
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), 
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), #pk - primary key
    path('about/', views.about, name='blog-about'), 
]

#PostListView.as_view() class view musi mieć template taki:
#<app>/<model>_<viewtype>.html w tym przypadku blog/post_list.html

# przekierowanie po kliknięciu w Post w PostCreateView i PostUpdateView jest zdefiniowane w models get_absolute_url
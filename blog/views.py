from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic import( 
                                ListView, 
                                DetailView, 
                                CreateView,
                                UpdateView,
                                DeleteView)
#from django.http import HttpResponse
from .models import Post # .model - bo jest w tym samym folderze

# jest kilka rodzajów class 
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # sortowanie postów względem dat

class PostDetailView(DetailView):
    model = Post


#LoginRequiredMixin to stusujemy w class base component i od razy nas przekierowuje do logowania
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        print(form)
        return super().form_valid(form) #wywołanie form_valid w clasie parent


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
    # z automatu ładude template z CreateView
    model = Post
    fields = ['title','content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        print(form)
        return super().form_valid(form) #wywołanie form_valid w clasie parent
    def test_func(self):
        post = self.get_object()
        print(self.request.user)
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/' # tylko to trzeba zdefiniować by po usunięciu posta przekierowało do home page , działa też na "/post/new"
    def test_func(self):
        post = self.get_object() # get_object pobiera aktualny post
        print(self.request.user)
        if self.request.user == post.author:
            return True
        return False

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    #return HttpResponse('<h1>Blog home</h1>')
    print(request)
    return render(request,'blog/home.html',context) # w html odnosimy sie nie do contex ale do posts

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})

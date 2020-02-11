from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete - jeśli usuniemy usera to usunięte zostaną wszystkie pjego posty
    #date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk}) # reverse zwraca fullurl jako string , 
        # nie możemy przekierować po dodatniu postu poprzez redirect tylko właśnie tak
        # self.pk - to primary key danego postu

    
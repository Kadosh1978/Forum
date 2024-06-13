from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    category_type = models.CharField(max_length = 255, unique = True)

    subscribers = models.ManyToManyField(User, blank=True, related_name='categories')

    def __str__(self):
        return self.category_type
    
class Post(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    head = models.CharField(max_length = 255, unique = True)
    text = models.TextField()
    category = models.ManyToManyField(Category, through="PostCategory")
    rating = models.IntegerField(default=0)

    def preview(self):
        return f'{self.text[:124]}...'
    
    def __str__(self):
        return f'Заголовок: {self.head.title()}: Дата публикации: {self.time_in}: Текст статьи:{self.text}'
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0)

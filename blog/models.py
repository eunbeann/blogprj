from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=10)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) #올린 날짜 자동 수정

    def __str__(self):
        return self.title

from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()
    url = models.URLField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('mysite.Post')

    def __str__(self):
        return self.text[:20]

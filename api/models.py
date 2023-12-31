from django.db import models


class User(models.Model):
    class Meta:
        app_label = 'api'

    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Post(models.Model):
    class Meta:
        app_label = 'api'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:50]}"

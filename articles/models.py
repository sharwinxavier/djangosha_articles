from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # Here, the author is defined as a foreign key from the model ' User'
    #incase the user doesn't upload any image, the default image is set for the article and blank=true specifies that it can be a null field


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...' #this function when called will return the first 50 characters of the body of an article
#in the above line, the + '...' concatenates the ... along with the first 50 characters!
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
class Picture(BaseModel):
    image = models.ImageField(upload_to='pics/')
    caption = models.CharField(max_length=25)
    # upvotes = models.IntegerField(default=0)
    def __str__(self):
        return self.caption
class Likes(BaseModel):
    count = models.PositiveIntegerField(default=0)
    upvotes = models.ManyToManyField(Picture,related_name='like')
class Comment(BaseModel):
    text = models.TextField()
    post = models.ForeignKey(Picture,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.text
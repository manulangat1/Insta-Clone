from django.db import models

# Create your models here.
class BaseModel(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
class Picture(BaseModel):
    image = models.ImageField(upload_to='pics/')
    caption = models.CharField(max_length=25)

    def __str__(self):
        return self.caption
class Comment(BaseModel):
    text = models.TextField()
    picture = models.ForeignKey(Picture,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.text
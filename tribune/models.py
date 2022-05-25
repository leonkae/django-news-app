from re import M 
from django.db import models

class Editor(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        return self.save()
    class Meta:
        ordering = ['first_name']
    
class tags(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
  
    






from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()


    def __str__(self) -> str:
        return self.username + ' '+ self.email
    

class Quotes(models.Model):
    author_name = models.CharField(max_length=50)
    quotes = models.TextField()


    def __str__(self) -> str:
        return self.author_name + ' '+ self.quotes


        
       

# Create your models here.

from django.db import models

class publication(models.Model):
    authors = models.CharField(max_length=100)
    title   = models.CharField(max_length=200)
    image   = models.ImageField(upload_to='images/',blank=True)
    where   = models.CharField(max_length =200)
    doi     = models.CharField(max_length =100, blank = True)
    year    = models.CharField(max_length = 10)
    description = models.TextField(blank=True)
    pubconf    = models.CharField(max_length=100,default='publication')
    pdf     = models.FileField(null=True)


    def __str__(self):
        return self.title + ' - ' + self.where

# class conference(models.Model):
#     authors = models.CharField(max_length=100)
#     title   = models.CharField(max_length=200)
#     image   = models.ImageField(upload_to='images/',blank=True)
#     where   = models.CharField(max_length =200)
#     year    = models.CharField(max_length = 10)
#     # description = models.TextField(blank=True)

#     def __str__(self):
#         return self.title + ' - ' + self.where        
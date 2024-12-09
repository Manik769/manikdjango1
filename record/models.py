from django.db import models

# Create your models here.
class User(models.Model):
    gender_filed=[
        ('male','Male'),
        ('female','Female')
    ]
    language_filed=[
        ('spanish','Spanish'),
        ('french','French'),
        ('english','English'),
    ]
    name = models.CharField(max_length=255)
    email= models.EmailField(max_length=255,unique=True)
    gender=models.CharField(choices=gender_filed,max_length=10,blank=True,null=True)
    language = models.CharField(choices=language_filed,max_length=100)
    country = models.CharField(max_length=100)
    image= models.ImageField(upload_to='images',blank=True,null=True)

    def get_language(self):
        lang=self.language
        lang_object=lang.split(',')
        return lang_object

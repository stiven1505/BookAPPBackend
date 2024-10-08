from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    
    class Meta:
        db_table = 'books'
    
    def __str__(self):
        return self.name

    
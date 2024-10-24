from django.db import models
class Product(models.Model):
    img = models.ImageField(upload_to='pics')
    pnmae = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    def __str__(self):
        return self.pnmae

    

    

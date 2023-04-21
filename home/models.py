from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField(default='')

    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.TextField(default='')
    image =models.ImageField(upload_to='images/',default='')
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    url = models.URLField(default='')
    downloads = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name

class Popular(models.Model):
    product= models.ForeignKey(Product,on_delete=models.CASCADE)

class Contact(models.Model):
    name=models.CharField(max_length=200,default='')
    email = models.EmailField()
    mobile_no= models.CharField(max_length=20)
    query = models.TextField(max_length=500)

class Feedback(models.Model):
    name=models.CharField(max_length=200,default='')
    email = models.EmailField()
    mobile_no= models.CharField(max_length=20)
    feedback= models.TextField(max_length=500)

class Coursal(models.Model):
    coursal_id = models.AutoField(primary_key=True)
    coursal_image = models.ImageField(upload_to="coursal_images", default="")
    image_url = models.URLField(default='')

    def str(self):
        return f"Coursal_Image {str(self.coursal_id)}"

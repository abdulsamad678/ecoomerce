from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class CATEGORY(models.Model):
     name= models.CharField(max_length=200)
     
     
    
     def __str__(self):
      return self.name

class Product(models.Model):
    name= models.CharField(max_length=200)
    price= models.IntegerField(default=0)
    category = models.ForeignKey(CATEGORY, on_delete=models.CASCADE, default=1)
    description= models.CharField(max_length=200)
    image= models.ImageField(upload_to="myimage")

    def __str__(self):
	    return self.name
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)






        


  
	



		

			
		
			







from django.db import models
from product.models import Item_product
# Create your models here.
#payment  credit_card wallet  order
# cash cart cart_product order_product 
from User.models import User

class Payment(models.Model):
    Payment_id = models.AutoField(primary_key=True)


class CreditCard(models.Model):
    Payment = models.OneToOneField(Payment, on_delete=models.CASCADE, blank=True, null=True)
    Card_Number = models.CharField(max_length=16, blank=True, null=True)
    CVV = models.CharField(max_length=4, blank=True, null=True)
    Card_password = models.CharField(max_length=20, blank=True, null=True)
    Exp_Date = models.DateField(blank=True, null=True)


class wallet(models.Model):
    Payment = models.OneToOneField(Payment, on_delete=models.CASCADE, blank=True, null=True)
    Phone_number = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    carreir = models.CharField(max_length=10, blank=True, null=True)


class Cash(models.Model):
    Payment = models.OneToOneField(Payment, on_delete=models.CASCADE, blank=True, null=True)
    Recieve_date = models.DateField(blank=True, null=True)


class Order(models.Model):
    Order_id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)
    Shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Adress = models.CharField(max_length=50, blank=True, null=True)
    #Total_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    Status = models.CharField(max_length=20, blank=True, null=True)


class Cart(models.Model):
    Cart_id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Total_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    Notes = models.TextField(blank=True, null=True)

class Cart_Product(models.Model):
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    Product = models.ForeignKey(Item_product, on_delete=models.CASCADE, blank=True, null=True)


class Order_Product(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    Product = models.ForeignKey(Item_product, on_delete=models.CASCADE, blank=True, null=True)
    Quantity = models.IntegerField( blank=True, null=True)
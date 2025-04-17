from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    product_code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Warranty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    warranty_code = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.warranty_code}"


from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

class Specification(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    products = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='specification')

class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    section = models.ForeignKey("Section", on_delete=models.CASCADE,blank=True, null=True)
    showcase = models.BooleanField(default=False)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    width = models.DecimalField(max_digits=6, decimal_places=2)
    height = models.DecimalField(max_digits=6, decimal_places=2)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20)
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE, related_name='orders')
    shipping = models.ForeignKey(Address, on_delete=models.CASCADE)

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    ref_no = models.CharField(max_length=255)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20)

class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='shippings')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)

class Shipment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    carrier = models.CharField(max_length=255)
    tracking_number = models.CharField(max_length=255)
    delivery_status = models.CharField(max_length=20)


#landing page 


class CarouselItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel/')
    product=models.ForeignKey(Product, on_delete=models.CASCADE)

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

class Policy(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

class AboutUs(models.Model):
    history = models.TextField()
    mission = models.TextField()
    team = models.TextField()


class Section(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel/')
    
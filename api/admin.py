from django.contrib import admin
from .models import  Address, ProductCategory, Specification, Product, CartItem, Order, OrderDetails, Payment, Shipping, Shipment, CarouselItem, FAQ, Policy, AboutUs, Section

admin.site.register(Address)
admin.site.register(ProductCategory)

# admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(CarouselItem)
admin.site.register(FAQ)
admin.site.register(Policy)
admin.site.register(AboutUs)

class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails
    extra = 0

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0

class ShippingInline(admin.TabularInline):
    model = Shipping
    extra = 0

class ShipmentInline(admin.TabularInline):
    model = Shipment
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at', 'status']
    inlines = [OrderDetailsInline, PaymentInline, ShippingInline, ShipmentInline]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'order', 'amount', 'payment_method', 'payment_date', 'payment_status']

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'city', 'state', 'zip_code']

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['order', 'carrier', 'tracking_number', 'delivery_status']




class SpecificationInline(admin.TabularInline):
    model = Specification
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [SpecificationInline]

admin.site.register(Product, ProductAdmin)

class SectionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Section, SectionAdmin)
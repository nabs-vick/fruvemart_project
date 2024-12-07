from django.contrib import admin
from .models import Customer,Category,Order,Product, Feedback, Cart_components
# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Feedback)
admin.site.register(Cart_components)

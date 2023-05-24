from django.contrib import admin
from purchase.models import *

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartDetail)
admin.site.register(Order)
admin.site.register(OrderDetail)

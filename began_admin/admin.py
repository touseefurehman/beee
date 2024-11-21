from django.contrib import admin

# Register your models here.
from .models import admin_product,FooterSetting,faqs,category,admin_products,about_us

admin.site.register(FooterSetting),
admin.site.register(admin_product),
admin.site.register(faqs),
admin.site.register(admin_products),
admin.site.register(about_us),
admin.site.register(category),
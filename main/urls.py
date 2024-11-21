from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="home" ),
    path("product/",views.product, name="products"),
    path("product_detail/",views.product_detail, name="product_detail"),
    path("inquire/",views.inquire, name="inquire"),
    path('footer/', views.footer, name='footer'),



]

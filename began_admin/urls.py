from django.urls import path
from . import views

urlpatterns = [
    path('footer_setting/', views.setting_for_footer, name='footer_setting'),
    path('product/', views.product, name='product'),
    path('category/', views.product_category, name='category'),
    path('filter-tag-page/', views.filter_tag_page, name='filter_tag_page'),
    path('faqs/', views.faqs_admin, name='faqs'),
    path('about-us/', views.about_us, name='about_us'),
    path('admin-product/', views.admin_product, name='admin_product'),
    path('footer_edit/', views.footer_edit,name='footer_edit'),
]

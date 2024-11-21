from django.db import models



class admin_product(models.Model):
    name = models.CharField(max_length=200)  # Product name
    image = models.ImageField(upload_to='product_images/')  # Product image
    stock = models.PositiveIntegerField()  # Stock quantity

    def __str__(self):
        return self.name






class FooterSetting(models.Model):
    about_us = models.TextField(blank=True, null=True)  
    contact_number = models.CharField(max_length=15)
    contact_email = models.EmailField(max_length=255, blank=True, null=True)  
    contact_information = models.TextField(blank=True, null=True)  
    showroom_address = models.TextField(blank=True, null=True)  
    company_logo = models.ImageField(upload_to='footer_logos/', blank=True, null=True)  
    website_linked_email_addresses = models.CharField(max_length=500, blank=True, null=True)  
    def __str__(self):
        return "Footer Settings"




class category(models.Model):
    category_name = models.CharField(max_length=100)
    feature_on_home = models.BooleanField(default=False)

    def __str__(self):
        return self.category_name

    
    
    
    
class faqs(models.Model):
    question = models.CharField(max_length=122)
    answer = models.CharField(max_length=245)
   

    def __str__(self):
     return self.question
 
 
 
 
    
class about_us(models.Model):
    file = models.FileField( upload_to="about_us_image",)
    link = models.CharField(max_length=999)
    oder = models.IntegerField()
    text = models.TextField(max_length=999) 
def __str__(self):
    return self.oder
 
 
 
 
 
 
class tag(models.Model):
    tag_name = models.CharField(max_length=70)



class admin_products(models.Model):
    prouct_name = models.CharField(max_length=70)
    product_image = models.ImageField(upload_to="product_image")
    product_videos = models.FileField(upload_to="product_video")
    description = models.TextField()
    key_featurs_name = models.CharField(max_length=70)
    key_featurs_image = models.ImageField(upload_to="key_featurs_image")
    key_featurs_description = models.CharField(max_length=780)
    Specification = models.TextField()
    e_bonchers_feature_name = models.CharField(max_length=780)
    e_bonchers_feature_image = models.ImageField(upload_to="e_bonchers_feature_image")
    applications = models.TextField()
    warranty = models.TextField()
    
def __str__(self):
    return self.product_name

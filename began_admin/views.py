from django.shortcuts import render,redirect
from .models import category,FooterSetting ,faqs # Import your model


def product_category (request):
    categories = category.objects.all()    
    if request.method == "POST":
        # Get the form data
        category_name = request.POST.get('category', '').strip()  
        feature_on_home = request.POST.get('home_feature') == 'on'
        # Save to the database
        category.objects.create(
            category_name=category_name,
            feature_on_home=feature_on_home
        )   
        categories = category.objects.all()
        print(categories)



    return render(request, 'admin/category.html', {"categories":categories})














def setting_for_footer (request):
    footer_data = FooterSetting.objects.first()
    print(footer_data)
    return render(request, 'admin/settings.html' ,{"footer_data":footer_data})




def product (request):
    return render(request, 'admin/products.html',)


def filter_tag_page (request):
    
    
    
    
    
    
    
    
    
    return render(request, 'admin/filter-tag-page.html',)





    


def faqs_admin (request):
    
    
    
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')

        if question and answer:  # Ensure both fields are filled
            faqs.objects.create(question=question, answer=answer)
        

    
    faqs_admin = faqs.objects.all()
    
    
    
    return render(request, 'admin/faqs.html',{"faqs_admin":faqs_admin})


def about_us (request):
    return render(request, 'admin/about-us.html',)






def admin_product (request):
    
    return render(request, 'admin/admin-product.html',)










def footer_edit (request):


    footer_data = FooterSetting.objects.first()

    return render(request, 'admin/footer_setting_edit.html',{"footer_data":footer_data})
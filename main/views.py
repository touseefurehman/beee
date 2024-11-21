from django.shortcuts import render
from began_admin.models import FooterSetting
# Create your views here.


def index(request):
    footer_data = FooterSetting.objects.first()
    
    return render(request, 'main/index.html',{'footer_data':footer_data})



def product(request):
    footer_data = FooterSetting.objects.first()

    return render(request, 'main/product.html',{'footer_data':footer_data})


def product_detail(request):
    footer_data = FooterSetting.objects.first()

    return render(request, 'main/productDetail.html',{'footer_data':footer_data})

def inquire(request):
    footer_data = FooterSetting.objects.first()

    return render(request, 'main/inquire.html',{'footer_data':footer_data})




def footer(request):
    
    footer_data = FooterSetting.objects.first()
    return render(request, 'base/main/footer_main.html',{'footer_data':footer_data})
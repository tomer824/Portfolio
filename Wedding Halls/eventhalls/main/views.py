from django.shortcuts import render, redirect

# Create your views here.

def main(request): 
    if request.user.is_authenticated:
        return redirect('router')   
    else:
        return render(request, 'main.html')

def contact_us(request):
    return render(request, 'contact-us.html')
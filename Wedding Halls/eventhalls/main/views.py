from django.shortcuts import render, redirect

# Create your views here.

def main(request): 
    if request.user.is_authenticated:
        return redirect('router')   
    else:
        return render(request, 'main.html')
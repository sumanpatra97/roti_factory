from django.shortcuts import render

from rotinew.models import rotii, login

def disp(request):
    return render(request,'home.html',)

def dispnav(request):
    user=request.GET['user']
    value = int(request.GET['value'])
    valuenew = value * 3
    rotii_info=rotii(user=user,value=value)
    rotii_info.save()
    return render(request,'order.html',{'user':user,'value':valuenew})

def memo(request):
    return render(request,'register.html')

def memory(request):
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    login_info=login(first_name=firstname,last_name=lastname)
    login_info.save()
    return render(request,'login.html')

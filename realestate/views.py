from django.shortcuts import render

# Create your views here.

def buy(request):
    return render(request,template_name='buy_features.html')

def rent(request):
    return render(request,template_name='rent_features.html')

def buyhome1(request):
    return render(request,template_name='b_feat_1.html')

def buyhome2(request):
    return render(request,template_name='b_feat_2.html')

def renthome1(request):
    return render(request,template_name='r_feat_1.html')

def renthome2(request):
    return render(request,template_name='r_feat_2.html')

def confirm(request):
    return render(request,template_name='confirm.html')

def agent_p(request):
    return render(request,template_name='CompanyProfile.html')


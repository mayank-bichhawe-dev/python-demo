from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('this is home page')
    context = {
        'name': 'mayank',
        'surname': 'khatri'
    }
    return render(request,'index.html', context)

def about(request):
    # return HttpResponse('this is about page')
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse('this is contact page')
    return render(request, 'contact.html')

def services(request):
    # return HttpResponse('this is services page')
    return render(request, 'service.html')
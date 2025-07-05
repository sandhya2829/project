from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    result = None;
    if request.method == 'POST':
        a = int(request.POST.get('Num1'))
        b = int(request.POST.get('Num2'))
        Op = request.POST.get('Op')
        if Op == 'add':
            result = a + b
        if Op == 'Sub':
            result = a - b
        if Op == 'mul':
            result = a * b
        else:
            return render(request,'home.html',{'error': 'error'})

        return render(request,'home.html',{'result':result})
    return render(request,'home.html')
def hello(request):
    return HttpResponse("hello")
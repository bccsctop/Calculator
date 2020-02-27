from django.shortcuts import render , redirect
from .models import History


def home_page (request):
    return render(request,'calculator/homepage.html')

def mepage (request):
    return render(request,'calculator/aboutme.html')


def index(request):

    if request.method == 'POST' and request.POST.get('input1','') and request.POST.get('input2','')  :
        
        #set variable
        x = request.POST.get('input1','')
        y = request.POST.get('input2','')

        #plus
        if request.POST.get('plus','') :
            operator = '+'
            result = float(x) + float(y)

        #subtract
        if request.POST.get('subtract',''):
            operator = '-'
            result = float(x) - float(y)   

        #multiple
        if request.POST.get('multiple',''):
            operator = '*'
            result = float(x) * float(y)

        #divide
        if request.POST.get('divide',''):
            operator = '/'
            result = float(x) / float(y)

        History.objects.create(input1=x , input2=y,result=result,operator=operator)
        all_history = History.objects.all()

        return render(request, 'calculator/index.html',{'result': str(result) ,'allhistory':all_history})
         

   
    return render(request, 'calculator/index.html')

def remove_history(request,id):
    History.objects.get(id=id).delete()
    all_history = History.objects.all()
    return render(request, 'calculator/index.html',{
         'allhistory':all_history})

def remove_all_history(request):
    allhistory = History.objects.all()
    allhistory.delete()
    return render(request,'calculator/index.html')

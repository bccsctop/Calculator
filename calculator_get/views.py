from django.shortcuts import render
from .models import History


def index (request):

    if request.method == 'GET' and request.GET.get('input1','') and request.GET.get('input2','')  :
        
        #set variable
        x = request.GET.get('input1','')
        y = request.GET.get('input2','')

        #plus
        if request.GET.get('plus','') :
            operator = '+'
            result = float(x) + float(y)

        #subtract
        if request.GET.get('subtract',''):
            operator = '-'
            result = float(x) - float(y)   

        #multiple
        if request.GET.get('multiple',''):
            operator = '*'
            result = float(x) * float(y)

        #divide
        if request.GET.get('divide',''):
            operator = '/'
            result = float(x) / float(y)


        History.objects.create(input1=x , input2=y,result=result,operator=operator)
        all_history = History.objects.all()

        return render(request, 'calculator/index.html',{'result': str(result) ,'allhistory':all_history})
         

    return render(request, 'calculator_get/index.html')


def remove_history(request,id):
    History.objects.get(id=id).delete()
    all_history = History.objects.all()
    return render(request, 'calculator/index.html',{
         'allhistory':all_history})

def remove_all_history(request):
    allhistory = History.objects.all()
    allhistory.delete()
    return render(request,'calculator/index.html')
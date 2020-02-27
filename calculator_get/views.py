from django.shortcuts import render


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


        return render(request, 'calculator_get/index.html',{'result': str(result) })

    return render(request, 'calculator_get/index.html')

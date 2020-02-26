from django.shortcuts import render , redirect



def index(request):

    if request.method == 'POST' and request.POST.get('input1','') and request.POST.get('input2','')  :
        #set variable
        x = request.POST.get('input1','')
        y = request.POST.get('input2','')

        #plus
        if request.POST.get('plus','') :
            result = float(x) + float(y)
            return render(request, 'calculator/index.html',{'result': result})

        #subtract
        if request.POST.get('subtract',''):
            result = float(x) - float(y)
            return render(request, 'calculator/index.html',{'result': result})

        #multiple
        if request.POST.get('multiple',''):
            result = float(x) * float(y)
            return render(request, 'calculator/index.html',{'result': result})

        #divide
        if request.POST.get('divide',''):
            result = float(x) / float(y)
            return render(request, 'calculator/index.html',{'result': result})
            
    return render(request,'calculator/index.html')
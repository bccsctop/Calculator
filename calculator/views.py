from django.shortcuts import render , redirect



def index(request):
    if request.method == 'POST' and request.POST.get('input1','') and request.POST.get('input2','')  :
        x=request.POST.get('input1','')
        y=request.POST.get('input2','')

        #plus
        if request.POST.get('plus','') :
            result= float(x)+float(y)
            return render(request, 'calculator/index.html',{'result': result})


    return render(request,'calculator/index.html')
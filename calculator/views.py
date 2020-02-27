from django.shortcuts import render , redirect


def home_page (request):
    return render(request,'calculator/homepage.html')




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

        
        return render(request, 'calculator/index.html',{'result': str(result) })
         

   
    return render(request, 'calculator/index.html')

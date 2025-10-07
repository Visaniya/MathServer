from django.shortcuts import render 
def calculate_bmi(request): 
    context={} 
    context['bmi'] = "0" 
    context['w'] = "0" 
    context['h'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        w=request.POST.get('Weight','1')
        h=request.POST.get('Height','1')
        print('request=',request) 
        print('Weight=',w) 
        print('Height=',h) 
        bmi=int(w)/((int(h)/100)**2)
        context['bmi'] = bmi
        context['w'] = w
        context['h'] = h
        print('BMI=',bmi) 
    return render(request,'myapp/math.html',context)
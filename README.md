# Ex.05 Design a Website for Server Side Processing
## Date:07/10/2025

## AIM:
 To design a website to calculate the the Body Mass Index (BMI) in the server side. 


## FORMULA:
BMI = W/H<sup>2</sup>
<br> BMI --> Body Mass Index 
<br> W --> Weight
<br> H --> Height

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<html> 
<head> 
    <title>Body Mass Index</title>
    <style>
        .head{
            gap:30;
            position:absolute;
            top:22%;
            right:40%;
            border: 5px black;
            border-radius: 20px;
            background: lavender;
        }
        input {
            margin-top: 5px;
            padding:5px;
            border-radius: 20px;
        }
        body{
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            background-color: lavender;
        }
        form {
            border-color: black;
            border-radius: 20px;
            width: 300px;
        }
        .submit{
            color:lavender;
            background-color: aqua;
        }
    </style> 
</head> 
<body>
    <centre>
    <div class="head">  
            <h1>Body Mass Index</h1>
            <h2>S.VISANIYA</h2> 
            <h3>25017540</h3>
    <form method="POST">
{%csrf_token %}
        <div class="formelt"> 
        Height:<input type="text" id="Height" name="Height" required></input>in cm<br> 
        </div> 
        <div class="formelt"> 
        Weight:<input type="text" id="Weight"name="Weight" required></input>in kg<br> 
        </div> 
        <div class="formelt"> 
        <input class="submit" type="submit" value="Calculate BMI"><br/> 
        </div> 
        <div class="formelt"> 
        BMI:<input type="text" name="bmi" value="{{bmi}}"></input>m<sup>2</sup><br> 
        </div>
    </form>
    </div>
    </div> 
</body>
</html>

views.py

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

    urls.py

    from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmi/',views.calculate_bmi,name="bmi"),
    path('',views.calculate_bmi, name="bmicalculator"),
]
```

## SERVER SIDE PROCESSING:
Screenshot (27).png

## HOMEPAGE:
Screenshot (26).png

## RESULT:
The program for performing server side processing is completed successfully.

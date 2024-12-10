from django.shortcuts import render
from .models import Game

# Create your views here.


def display(request):
    data= Game.objects.all()
    context={
    'data':data
    }
    return render(request,'index.html',context)
 
def details(request,pk):
    data1=Game.objects.get(id=pk)
    context={
        'data1':data1
    }
    return render(request,'single_details.html',context)

def update(request,jp):
    data2=Game.objects.get(id=jp)
    if request.method == "POST":
        name=request.POST.get('name')
        place=request.POST.get('place')
        thing=request.POST.get('thing')
        number=request.POST.get('number')
       
        print(name,place,thing,number)
        data2.name=name
        data2.place=place
        data2.thing=thing
        data2.number=number
        data2.save()
        # print(name,place,thing,number)
    context={
        'data2':data2
    }
    return render(request,'edit.html',context)


    
        
